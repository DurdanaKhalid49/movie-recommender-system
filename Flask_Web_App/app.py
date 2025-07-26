from flask import Flask, request, render_template
import pandas as pd
import joblib
from huggingface_hub import hf_hub_download

app = Flask(__name__)

# Download from HF and load
movies_path = hf_hub_download(repo_id="durdanakhalid/movie-recommender-models", filename="movies.pkl")
similarity_path = hf_hub_download(repo_id="durdanakhalid/movie-recommender-models", filename="similarity.pkl")
vectorizer_path = hf_hub_download(repo_id="durdanakhalid/movie-recommender-models", filename="vectorizer.pkl")

movies = joblib.load(movies_path)
similarity = joblib.load(similarity_path)
vectorizer = joblib.load(vectorizer_path)


def recommend(movie, num_recommendations=10):
    movie = movie.lower()
    if movie not in movies['title'].str.lower().values:
        return ["Movie not found."]
    
    index = movies[movies['title'].str.lower() == movie].index[0]
    distances = list(enumerate(similarity[index]))
    distances = sorted(distances, reverse=True, key=lambda x: x[1])[1:num_recommendations+1]

    recommended_movies = [movies.iloc[i[0]].title for i in distances]
    return recommended_movies

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    movie_name = ''
    if request.method == 'POST':
        movie_name = request.form['movie']
        recommendations = recommend(movie_name)

    return render_template('index.html', recommendations=recommendations, movie_name=movie_name)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # use Railway port or default to 8080
    app.run(host="0.0.0.0", port=port) 
