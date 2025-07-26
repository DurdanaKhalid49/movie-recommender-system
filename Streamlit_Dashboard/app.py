import streamlit as st
# import pandas as pd
import joblib

# Load saved model components
pipeline = joblib.load("model/vectorizer.pkl")
similarity = joblib.load("model/similarity.pkl")
movies_df = joblib.load("model/movies.pkl")  # Save this DataFrame separately during training

# Set page config
st.set_page_config(page_title="🎬 Movie Recommender", layout="centered")

# App title
st.title("🎬 Movie Recommender System")
st.markdown("Get similar movies based on what you like!")

# Input
movie_name = st.text_input("Enter a movie name", "")
top_n = st.slider("Number of recommendations", min_value=1, max_value=15, value=5)

def recommend(movie, n=5):
    movie = movie.lower()
    if movie not in movies_df['title'].str.lower().values:
        return []
    index = movies_df[movies_df['title'].str.lower() == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended = [movies_df.iloc[i[0]].title for i in distances[1:n+1]]
    return recommended

if st.button("Recommend"):
    if movie_name.strip() == "":
        st.warning("Please enter a valid movie name.")
    else:
        recs = recommend(movie_name, top_n)
        if recs:
            st.success(f"Movies similar to '{movie_name.title()}':")
            for movie in recs:
                st.markdown(f"✅ **{movie}**")
        else:
            st.error("Movie not found in database. Try a different title.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Created by Durdana Khalid &copy; 2025</p>",
    unsafe_allow_html=True
)
