from flask import Flask, request, render_template
import pandas as pd
import joblib

app = Flask(__name__)

# Load model files
movies = pd.read_csv('model/movies.csv')
similarity = joblib.load('model/similarity.pkl')

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

if __name__ == '__main__':
    app.run(debug=True)
