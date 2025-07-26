# 🎬 Movie Recommender System - Flask Web App

This is a Flask-based web application that recommends movies similar to the one you enter. It uses NLP techniques and cosine similarity to provide content-based recommendations.

## 📌 Features

- Clean, modern, and mobile-responsive UI
- Enter a movie name and get similar suggestions
- Trained using TMDB 5000 Movie & Credits Dataset
- Deployed using [Railway](https://railway.app/)

## 🚀 Live Demo

🔗 [Visit Web App](https://customer-churn-prediction-production-aac3.up.railway.app/)  
*(Replace with your deployed URL once available)*

## 🧠 How It Works

1. The movie metadata is processed to extract relevant features (`overview`, `genres`, `cast`, `crew`, etc.).
2. Text data is combined and vectorized using CountVectorizer.
3. Cosine similarity is computed between vectors.
4. Flask displays the recommended movies on a stylish webpage.

## 🗃️ Project Structure
```
Movie_Recommender_System/
│
├── Flask_Web_App/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ ├── model/
│ │ ├── recommender_pipeline.joblib
│ │ ├── similarity_matrix.joblib
│ │ └── movies_df.joblib
│ └── requirements.txt
```

## ⚙️ Installation (Local)

### 1. Clone the repository  
```bash
git clone https://github.com/DurdanaKhalid49/customer-churn-prediction.git
cd customer-churn-prediction/Flask_Web_App
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
python app.py
```
📦 Requirements
Flask

pandas

scikit-learn

joblib

👩‍💻 Author
Durdana Khalid
📫 LinkedIn
🐙 GitHub
