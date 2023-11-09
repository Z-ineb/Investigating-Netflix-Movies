# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Start coding!
#Load the CSV file and store as netflix_df
netflix_df= pd.read_csv('netflix_data.csv')

#Filter the data to remove TV shows 
netflix_subset=netflix_df[netflix_df["type"]!="TV Show"]

#Investigate the Netflix movie data, keeping only the columns "title", "country", "genre", "release_year", "duration"
netflix_movies=netflix_subset[["title", "country", "genre", "release_year", "duration"]]

#print(netflix_movies)

#Filter netflix_movies to find the movies that are shorter than 60 minutes
short_movies=netflix_movies[netflix_movies["duration"]<60]


colors=[]
for index, movie in netflix_movies.iterrows():
    if movie['genre']=='Children':
        colors.append("red")
    elif movie['genre']=='Documentaries':
        colors.append("blue")
    elif movie['genre']=='Stand-Up':
        colors.append("green")
    else:
        colors.append("black")
        
#print(colors)

##plot
fig=plt.figure(figsize=(12,8))
                        
plt.scatter(netflix_movies.release_year,netflix_movies.duration,c=colors)
                               
plt.xlabel("Release year")
plt.ylabel("Duration (min)")
plt.title("Movie Duration by Year of Release")
plt.show()

answer="maybe"
