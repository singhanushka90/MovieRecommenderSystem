import streamlit as st
import pickle
import pandas as pd

# ----------------- Load Data -----------------
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ----------------- Recommendation Function -----------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]cd
    return [movies.iloc[i[0]].title for i in movies_list]

# ----------------- Streamlit UI -----------------
st.set_page_config(page_title="🎬 Movie Recommender", layout="wide")

# Sidebar
st.sidebar.title("🎬 Movie Recommender ")
st.sidebar.write("Use this app to get top 5 similar movies based on your choice.")
menu = st.sidebar.radio("Navigate", ["Home", "Recommend", "About"])

# Home Page
if menu == "Home":
    st.title("🎥 WELCOME to the Movie Recommender System")
    st.write("""
    This app recommends movies based on **content similarity**.  
    Select a movie and get 5 best similar recommendations instantly!
    """)

# Recommendation Page
elif menu == "Recommend":
    st.title("🔎 Get Movie Recommendations")
    movie_list = movies['title'].values
    selected_movie = st.selectbox("Select a movie:", movie_list)

    if st.button("Recommend"):
        recommendations = recommend(selected_movie)
        st.subheader("📌 Top 5 Recommended Movies:")
        for i, movie in enumerate(recommendations, 1):
            st.write(f"{i}. {movie}")

# About Page
elif menu == "About":
    st.title("ℹ️ About This Project")
    st.write("""
    - Built with **Python, Streamlit & Machine Learning**  
    - Uses **TfidfVectorizer + Cosine Similarity** for recommendations  
    - Trained on a sample movie dataset  

    👩‍💻 Developer: *Anushka Singh*  
    """)
