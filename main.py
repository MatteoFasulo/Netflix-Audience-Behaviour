from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
import requests
import os
import random
from dotenv import load_dotenv

import pandas as pd
import numpy as np

from implicit.als import AlternatingLeastSquares
from implicit.nearest_neighbours import bm25_weight
from scipy.sparse import csr_matrix, save_npz, load_npz

load_dotenv()
TMDB_API_KEY = os.getenv('TMDB_API_KEY')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get('/')
def home(request: Request, n: int = 8):
    rec_sys = RecommendationSystem()

    user_id = random.randint(0, 109760)
    recommendations = rec_sys.get_user_recommendations(user_id, n)
    return templates.TemplateResponse("recommendations.html", {"request": request, "recommendations": recommendations})

@app.get('/recommendations/{user_id}')
def get_recommendations(request: Request, user_id: int, n: int = 8):
    # Call your recommendation function and get recommendations for the user
    rec_sys = RecommendationSystem()

    recommendations = rec_sys.get_user_recommendations(user_id, n)

    return {"recommendations": recommendations}

class RecommendationSystem:
    def __init__(self):
        self.df = pd.read_csv('vodclickstream_uk_movies_03.csv', encoding='utf-8', index_col=0)
        self.model = AlternatingLeastSquares(factors=32, regularization=0.01, iterations=10).load('netflix_als_model')
        self.sparse_user_item = load_npz('sparse_user_item.npz')

    def get_user_recommendations(self, user_id: int, n: int):
        # Get recommendations for the user from your ALS model
        movie_ids, scores = self.model.recommend(user_id, self.sparse_user_item[user_id], N=n, filter_already_liked_items=True)

        # Extract the item IDs from the recommendations
        rec_df = self.df.iloc[movie_ids].copy()
        rec_df['score'] = scores
        rec_df = rec_df.sort_values('score', ascending=False)
        rec_df = rec_df[['title', 'release_date', 'genres', 'movie_id']]
        rec_df = rec_df.drop_duplicates()

        def get_poster(movie_title: str, movie_year: int):
            # Search movie in TMDB API
            url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1&year={movie_year}"

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {TMDB_API_KEY}"
            }

            response = requests.get(url, headers=headers)

            response = response.json()

            results = response.get('results')

            try:
                movie_details = results[0]
            except IndexError:
                return '...'

            poster_url = f'http://image.tmdb.org/t/p/original{movie_details.get("poster_path")}'
            overview = movie_details.get('overview')

            return poster_url, overview

        rec_df[['poster', 'overview']] = rec_df.apply(lambda row: get_poster(row['title'], row['release_date']), axis=1, result_type='expand')

        return rec_df.to_dict(orient='records')


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)