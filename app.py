import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
  ind = movies[movies['title']==movie].index[0]
  distances = similarity[ind]
  movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  rec_movies = []
  #recommended_movie_posters = []
  for i in movies_list:
    #movie_id = movies.iloc[i[0]].movie_id
    #recommended_movie_posters.append(fetch_poster(movie_id))
    rec_movies.append(movies.iloc[i[0]].title)
  return rec_movies

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

movie_selected = st.selectbox('Search a movie', movies['title'].values)

if st.button('Recommend'):
    recs = recommend(movie_selected)
    for i in recs:
      st.write(i)
