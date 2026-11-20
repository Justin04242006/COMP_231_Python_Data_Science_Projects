#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:13:29 2026

@author: justinpeabody
"""

import numpy as np
import pandas as pd

#Reading in and inspecting the data
Songs_1980s_data=pd.read_csv('/Users/justinpeabody/Desktop/COMP_231/In_class_data_projects/COMP_231_Data_Science_Mini_Projects/1980sClassics.csv')

print(Songs_1980s_data.head())


#Question 1: How does the happiness of songs change over the decade?

sum(Songs_1980s_data[]

valid_values=Songs_1980s_data[Songs_1980s_data.notnull()] #Checking globally for null values. valid_values has the same dimensions as the original dataset, indicating there are no null values.

Avg_valence_per_year=Songs_1980s_data.groupby('Year').agg(Average_valence=('Valence', 'mean')).reset_index() #Aggreagating the dataframe to calculate the average valence within each year. reset_index() changes Year from an index into a normal column so that it appears in the output file. 


path='/Users/justinpeabody/Desktop/COMP_231/In_class_data_projects/COMP_231_Data_Science_Mini_Projects/'

Avg_valence_per_year.to_csv(path + 'Avg_valence_per_year.csv', index=False) #Writing the aggregated dataset as a csv filethat does not include index columns (only actual columns)



#Question 2: How does duration of track relate to danceability?


#Converting the duration column into seconds via the creation of a new column

Songs_1980s_data[['Minutes', 'Seconds']]=Songs_1980s_data['Duration'].str.split(':', expand=True) #Creating new columns representing the minute and second portions of the duration (the portions of the duration column to the left and the right of the colon, respectively)

Songs_1980s_data['Duration(seconds)']=(Songs_1980s_data["Minutes"].astype(int)*60)+Songs_1980s_data["Seconds"].astype(int) #Creating a total duration in seconds column based on the minute and second columns


def duration_category(minutes):
    if minutes < 1:
        return "<1 min"
    elif minutes >= 1 and minutes <3:
        return "1-3 min"
    elif minutes >=3 and minutes <5:
        return "3-5 min"
    elif minutes >= 5:
        return ">5 min"
    
Songs_1980s_data['Duration_Category']=Songs_1980s_data['Minutes'].astype(int).apply(duration_category) #Applying a custom function to the Minutes column to categorize each track based on duration

Top_5_danceable_songs_per_duration_category=Songs_1980s_data.groupby('Duration_Category').apply(lambda x: x.nlargest(5, 'Danceability')).reset_index(drop=True)

        

Songs_1980s_data.set_index(['Duration_Category'])



columns=['Track', 'Artist', 'Duration', 'Danceability']

Less_than_1_minute=Top_5_danceable_songs_per_duration_category.loc[Top_5_danceable_songs_per_duration_category.Duration_Category=="<1 min"] #Dividing the dataframe into separate dataframes based on the value of the duration_category variable

One_to_3_mins=Top_5_danceable_songs_per_duration_category.loc[Top_5_danceable_songs_per_duration_category.Duration_Category=="1-3 min"]

Three_to_5_mins=Top_5_danceable_songs_per_duration_category.loc[Top_5_danceable_songs_per_duration_category.Duration_Category=="3-5 min"]

More_than_5_mins=Top_5_danceable_songs_per_duration_category.loc[Top_5_danceable_songs_per_duration_category.Duration_Category==">5 min"]


Top_5_danceability=pd.concat([pd.DataFrame([['<1 min', "", "", ""]], columns=columns),
                             Less_than_1_minute.reset_index(drop=True), 
                             pd.DataFrame([["1-3 mins", "", "", ""]], columns=columns),
                             One_to_3_mins.reset_index(drop=True), 
                             pd.DataFrame([["3-5 mins", "", "", ""]], columns=columns),
                             Three_to_5_mins.reset_index(drop=True),
                             pd.DataFrame([['>5 mins', '', '', '']], columns=columns),
                             More_than_5_mins.reset_index(drop=True)]) #Recombining the separate datasets back into a dataframe containing section headings for each level of duration_category
                             


Top_5_danceability.to_csv(path+ 'Top_5_danceability.csv', index=False)



#Question 3: Are high-tempo songs more popular?


All_tempo_measurements=np.array(Songs_1980s_data['Tempo']) #Extracting the tempo of all the songs as a Numpy array
Median_tempo=np.median(All_tempo_measurements) #Calculating the median of the tempo array


def tempo_category(tempo):
    if tempo <= Median_tempo:
        return "Low"
    elif tempo > Median_tempo:
        return "High"
    
    
Songs_1980s_data['Tempo_Category']=Songs_1980s_data['Tempo'].astype(float).apply(tempo_category) #Applying a custom function to the Tempo column to categorize each track as low or high tempo based on the median tempo in the dataset


Average_popularity_per_tempo_category=Songs_1980s_data.groupby('Tempo_Category').agg(Average_popularity=('Popularity', 'mean')).reset_index()

Average_popularity_per_tempo_category=(Average_popularity_per_tempo_category.sort_values(by='Average_popularity', ascending=False).reset_index(drop=True)) #Sorting the aggregated dataframe by average popularity in descending order


columns=['Tempo_Category', 'Average_popularity']

Avg_popularity_tempo_dataframe=pd.concat([pd.DataFrame([['Even year average popularity scores in descending order', '']], columns=columns),
Average_popularity_per_tempo_category])

Avg_popularity_tempo_dataframe.to_csv(path+ 'Tempo_popularity.csv', index=False)



#Question 4: Which artists have the highest proportion of danceable songs?


Songs_per_artist=Songs_1980s_data.groupby('Artist').aggregate('count').reset_index() #Counting the number of tracks produced by each artist in the dataset


def Danceability_indicator_function(danceability):
    if danceability > 0.7:
        return True
    elif danceability <= 0.7:
        return False


Songs_1980s_data['Danceable_indicator']=Songs_1980s_data['Danceability'].astype(float).apply(Danceability_indicator_function) #Creating a new boolean column that outputs True if the song is highly danceable and False if not (this will allow me to add up the danceable songs per artist because True=1 and False=0)


Danceable_songs_per_artist=Songs_1980s_data.groupby(['Artist', 'Danceable_indicator']).aggregate('count').reset_index() #Counting the number of highly danceable and not highly danceable songs per artist in the dataset

Danceable_songs_per_artist=Danceable_songs_per_artist.loc[Danceable_songs_per_artist['Danceable_indicator']==True, ['Artist', 'Track']] #Filtering highly danceable songs
Danceable_songs_per_artist.rename(columns={'Track': 'Highly_danceable_songs'}, inplace=True)
Songs_per_artist.rename(columns={'Track': 'Total_songs'}, inplace=True)

Songs_per_artist=Songs_per_artist[['Artist', 'Total_songs']] #Extracting the artist and Total_songs columns from the dataset of total songs per artist

Danceability_joined_dataset=pd.merge(Songs_per_artist, Danceable_songs_per_artist) #Joining the dataset of total songs per artist to the dataset of highly danceable songs per artist

Danceability_joined_dataset['Percent_danceable']=Danceability_joined_dataset['Highly_danceable_songs']/Danceability_joined_dataset['Total_songs']*100 #Creating a new column in the joined dataset representing the percentage of each artists's songs that are highly danceable

Danceability_joined_dataset=(Danceability_joined_dataset.sort_values(by='Percent_danceable', ascending=False).reset_index(drop=True)) #Sorting the percent_danceable values in descending order

Danceability_joined_dataset.to_csv(path+ 'danceable_artists.csv', index=False)

