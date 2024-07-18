import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    # Get the index of the movie
    movie_index = moviess[moviess['title'] == movie].index[0]
    # Get the similarity scores for that movie
    distances = similarity[movie_index]
    # Get a list of similar movies
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(moviess.iloc[i[0]].title)

    return recommended_movies

# Load the movies and similarity data
moviess = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Ensure moviess is a DataFrame
moviess = pd.DataFrame(moviess)

st.title("MOVIE RECOMMENDER SYSTEM")

# Select a movie from the dropdown
selected_movie_name = st.selectbox(
    "Select a movie:",
    moviess['title'].values
)

st.write("You selected:", selected_movie_name)

# Recommend movies on button click
if st.button("Recommend"):
    recommendations = recommend(selected_movie_name)
    st.write("Recommended movies:")
    for i in recommendations:
        st.write(i)
