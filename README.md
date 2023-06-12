# Recommendation System with Implicit ALS

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/downloads/release/python-370/)
[![FastAPI Version](https://img.shields.io/badge/fastapi-0.68.1-green)](https://fastapi.tiangolo.com/)
[![Uvicorn Version](https://img.shields.io/badge/uvicorn-0.17.4-yellow)](https://www.uvicorn.org/)
[![License](https://img.shields.io/badge/license-Apache2-blue.svg)](https://opensource.org/licenses/apache-2)

A powerful recommendation system built with implicit Alternating Least Squares (ALS) algorithm, using the watch history data from Netflix UK. The system provides personalized movie recommendations based on user preferences and exposes an API route with FastAPI for easy integration into your applications.

The recommendation system is trained on a dataset containing the watch history of over 109,761 users and 7,634 movies. By leveraging the power of ALS, it can generate accurate recommendations by analyzing user-item interactions.

## Features

- Retrieve movie recommendations for a specific user
- Generate movie suggestions based on user's watch history
- Expose recommendations through a FastAPI API route
- Render recommendations in a user-friendly web page using Jinja2 templates
- Show movie details including title, description, genres, and release date
- Utilize the TMDB API for fetching movie posters and additional details

## Prerequisites

Before running the recommendation system, make sure you have the following requirements installed:

- Python 3.7 or above
- FastAPI 0.68.1 or above
- Uvicorn 0.17.4 or above
- Pandas
- NumPy
- Implicit
- Requests
- Python-dotenv

## Getting Started

Follow the steps below to set up and run the recommendation system:

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/MatteoFasulo/Netflix-Audience-Behaviour.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Netflix-Audience-Behaviour
   ```

3. Install the required dependencies using pip:

   ```shell
   pip install -r requirements.txt
   ```

4. Obtain a TMDB API key by creating an account on the [TMDB website](https://www.themoviedb.org/) and create a `.env` file in the project directory. Add the following line to the `.env` file, replacing `<YOUR_TMDB_API_KEY>` with your actual TMDB API key:

   ```text
   TMDB_API_KEY=<YOUR_TMDB_API_KEY>
   ```

5. Start the recommendation system server using Uvicorn:

   ```shell
   uvicorn main:app --reload
   ```

6. Open your web browser and navigate to `http://127.0.0.1:8000` to access the recommendations web page.

## API Usage

The recommendation system exposes an API route to retrieve recommendations for a specific user. Use the following endpoint:

```
GET /recommendations/{user_id}?n={num}
```

- `user_id` (required): The ID of the user for whom you want to get recommendations.
- `num` (optional): The number of movie recommendations to generate (default: 8).

Example API request:

```
GET /recommendations/123?n=5
```

Example API response:

```json
{
  "recommendations": [
    {
      "title": "Movie 1",
      "release_date": "2022-01-01",
      "genres": "Action, Thriller",
      "

movie_id": 1234,
      "poster": "http://image.tmdb.org/t/p/original/poster1.jpg",
      "overview": "Movie 1 is an exciting action-packed thriller."
    },
    {
      "title": "Movie 2",
      "release_date": "2023-03-15",
      "genres": "Drama, Romance",
      "movie_id": 5678,
      "poster": "http://image.tmdb.org/t/p/original/poster2.jpg",
      "overview": "Movie 2 is a heartwarming drama with a touch of romance."
    },
    ...
  ]
}
```

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [Apache2 License](LICENSE).

🎬 Happy movie recommendations! 🍿🎉