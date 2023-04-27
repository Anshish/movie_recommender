import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{movie_id}?api_key=7c2d48cf7426d82f447196e40fd601fb')
    data=response.json()
    return data[poster_path]

def get_recommendations(movie):
    movie_index=original_data[original_data['title']==movie].index[0]
    distances=tf_similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]

    url='https://image.tmdb.org/t/p/original'
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        idx=original_data.iloc[i[0]].id
        recommended_movies.append(original_data.iloc[i[0]].title)
        recommended_movies_posters.append(url+original_data.iloc[i[0]].poster_path)
    return recommended_movies,recommended_movies_posters


# this is the data from content based algo
more_info=pickle.load(open('more_info.pkl','rb'))

# this tf_similarity matrix from content based algo
content_similarity=pickle.load(open('content_similarity.pkl','rb'))

index = more_info[more_info['title'] == 'Spirited Away'].index[0]
id = more_info[more_info['title'] == 'Spirited Away'].iloc[0]['id']

print(more_info.iloc[index]['id'])

#
# genre=original_data.iloc[index]['genres']
# print(genre)
#
# cast=original_data.iloc[index]['cast']
# print(cast)
#
# overview=original_data.iloc[index]['overview']
# print(overview)

