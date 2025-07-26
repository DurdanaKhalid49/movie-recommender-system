# 🎬 Movie Recommender System - Streamlit Dashboard

This is a modern and interactive Streamlit dashboard that recommends movies based on content similarity. It uses NLP and cosine similarity to generate recommendations from TMDB movie metadata.

## 📌 Features

- Sleek and minimal user interface
- Real-time movie recommendations with adjustable suggestions
- Built with Streamlit for fast interaction and simple deployment
- Model built using CountVectorizer + Cosine Similarity

## 🚀 Live Demo

🔗 [Streamlit App](https://your-streamlit-app-url.streamlit.app)  
*(Replace with your deployed Streamlit link)*

## 🧠 How It Works

1. Metadata (`genres`, `cast`, `crew`, etc.) is extracted and preprocessed.
2. CountVectorizer is used to convert tags into numerical vectors.
3. Cosine similarity matrix helps find the most similar movies.
4. Streamlit dashboard shows real-time recommendations.

## 🗃️ Project Structure
```bash
Movie_Recommender_System/
│
├── streamlit_app/
│ ├── app.py
│ ├── model/
│ │ ├── recommender_pipeline.joblib
│ │ ├── similarity_matrix.joblib
│ │ └── movies_df.joblib
│ └── requirements.txt
```

## ⚙️ Installation (Local)

### 1. Clone the repository  
```bash
git clone https://github.com/DurdanaKhalid49/movie-recommender-system.git
cd movie-recommender-system/Streamlit_Dashboard
```
### Create and activate virtual environment
```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run the app

```bash
streamlit run app.py
```
📦 Requirements
streamlit

pandas

scikit-learn

joblib

👩‍💻 Author
Durdana Khalid
📫 LinkedIn
🐙 GitHub

⭐ If you like this project, please star the repository and share your feedback!
