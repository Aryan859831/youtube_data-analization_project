#!/usr/bin/env python
# coding: utf-8

# In[5]:

import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import plotly.express as px
import time
import os

df = pd.read_csv('aggregeted_metrice_by_country.csv', sep = r'[\t]', engine = 'python')
df.columns


df2 = pd.read_csv('youtube_video_performence.csv', sep = r'[\t]', engine = 'python')
df2.columns


if __name__ == "__main__":
  df_fr_mrg = pd.read_csv('aggregeted_metrice_by_country.csv', sep = r'[\t]', engine = 'python', usecols = ['Views', "Video Title","Is Subscribed","Video Likes Added","User Subscriptions Added","User Subscriptions Removed"])
  df2_fr_merge = pd.read_csv('youtube_video_performence.csv', sep = r'[\t]', engine = 'python', usecols = ['Views', "Video Title","User Subscriptions Added","Video Likes Removed","Average View Percentage","User Subscriptions Removed","Video Likes Added","Date"])




# done parsing in datetime object

 
  


#understanding datasets
if __name__ == "__main__":
  df.columns
  df2.columns
  df2.head()
  df.tail()


#fixing NaN values
if __name__ == "__main__":
  df.isna().sum()
  df.dropna(inplace = True)
  df.bfill(inplace = True)
  df.isna().sum()

# In[19]:
if __name__ == "__main__":
  df2.isna().sum()
  df2.dropna(inplace = True)
  df2.bfill(inplace = True)
  df2.isna().sum()

  df.describe()
  df2.describe()


#calculating the likes which are not being removed
def likes_not_removed_df2():
  df2["dislike_cancel"] = df2["Video Likes Added"] -  df2["Video Likes Removed"]
  df2["dislike_cancel"].sum()


if __name__ == "__main__":
  for_pie1 = df[0:20]
  for_pie2 = df2[0:20]


#visualizations
def pie_for_views_by_subscription_added(for_pie2):
  fig = px.pie(for_pie2, values='Views', names='User Subscriptions Added', title='', color_discrete_sequence=px.colors.sequential.RdBu)
  return fig

def pie_for_views_by_video_likes_added(for_pie1):
  fig = px.scatter(for_pie1, x = "Views", y = 'Video Likes Added')
  return fig 
#insight:
#more views dosent affect the "how much likes are being added from the viewrs", that [much].


# In[28]:
if __name__ == "__main__":
  print(df["User Comments Added"].var())



#for distributional visualizations
def histplot_for_subscription_by_views(df2):
  sns.histplot(data=df2, x= 'User Subscriptions Added', y = 'Views',  hue="Views",  kind="kde", warn_singular=False)
  return plt


#for realational visualizations
def relplot_for_subscription_by_views(df2):
  sns.relplot(data=df2, x= 'User Subscriptions Added', y = 'Views',  hue="Views")
  return plt

# In[30]:

#adding a new column for better anlysis
if __name__ == "__main__":
  df2["Days"] = df2["Date"].dt.day_name()
  df2["Days"]
  df2.head()
  



#Question: who is my core audience and what are they intrested in?
if __name__ == "__main__":
  core_audience = df["Country Code"].value_counts()

#visualization for better perspecctive
def lineplot_for_Countrycode_by_subscriptionadded(df):
  fig = px.line(df, x="Country Code", y="User Subscriptions Added", title='Core Audiences', color = "Country Code")
  fig.show()
#core audiences is in US realted to this graph.


top_5_country_core_most_subs = df.groupby("Country Code")["User Subscriptions Added"].max()
top_5_country_core_most_views = df.groupby("Country Code")["Views"].max()
top_5_country_core_most_video_likes_added = df.groupby("Country Code")["Video Likes Added"].max()
top_5_country_core_most_Video_Dislikes_Added = df.groupby("Country Code")["Video Dislikes Added"].max()


# Convert to DataFrame
top_5_country_core_most_subs = top_5_country_core_most_subs.reset_index()
top_5_country_core_most_views = top_5_country_core_most_views.reset_index()
top_5_country_core_most_video_likes_added = top_5_country_core_most_video_likes_added.reset_index()
top_5_country_core_most_Video_Dislikes_Added= top_5_country_core_most_Video_Dislikes_Added.reset_index()




# Sort by relitive column
top_5_country_core_most_subs = top_5_country_core_most_subs.sort_values(by="User Subscriptions Added", ascending=False).head(15)
top_5_country_core_most_views = top_5_country_core_most_views.sort_values(by = "Views", ascending = False).head(10)
top_5_country_core_most_video_likes_added = top_5_country_core_most_video_likes_added.sort_values(by = "Video Likes Added", ascending = False).head(10)
top_5_country_core_most_Video_Dislikes_Added = top_5_country_core_most_Video_Dislikes_Added.sort_values(by = "Video Dislikes Added", ascending = False).head(15)



def piechart_for_country_with_most_subcription_added(top_5_country_core_most_subs):
  fig = px.pie(top_5_country_core_most_subs, values='User Subscriptions Added', names='Country Code', title =' Top 15 Countries by User Subscriptions Added', color_discrete_sequence = px.colors.sequential.Magma)
  return fig

def piechart_for_country_with_most_views(top_5_country_core_most_views):
  fig2 = px.pie(top_5_country_core_most_views,values ="Views" , names='Country Code', title = "Top 10 countries by views",color_discrete_sequence = px.colors.sequential.Plasma)
  return fig2

def piechart_for_country_with_most_video_likes_added(top_5_country_core_most_video_likes_added):
  fig3 = px.pie(top_5_country_core_most_video_likes_added, values ="Video Likes Added" , names='Country Code', title = "Top 10 countries by video likes added", color_discrete_sequence =px.colors.qualitative.Pastel1)
  return fig3

def piechart_for_country_with_most_video_dislikes_added(top_5_country_core_most_Video_Dislikes_Added):
  fig4 =  px.pie(top_5_country_core_most_Video_Dislikes_Added, values ="Video Dislikes Added" , names='Country Code', title = "Top 15 countries by most Dislikes given", color_discrete_sequence = px.colors.qualitative.Bold)
  return fig4





def videos_growth():
  df2["Date"] = pd.to_datetime(df2["Date"], errors="coerce", )
  df2["date_formatted"] = df2["Date"].dt.strftime("%d-%b-%y")

  top_growth = df2.groupby(df2["date_formatted"]).agg({
  'Views' : "max",
  'Video Likes Added' : "max",
  'Video Dislikes Added' : "min",
  'Video Likes Removed' : "min",
  'Average View Percentage' : "max",
  'Average Watch Time' : "max",
  'User Comments Added' : "max",
  'User Subscriptions Added' : "max",
  'User Subscriptions Removed' : "min"    
  }).reset_index().sort_values(by="User Subscriptions Added", ascending=False).head(20)
  return top_growth


def videos_growth_no_head():
  df2["Date"] = pd.to_datetime(df2["Date"], errors="coerce", )
  df2["date_formatted"] = df2["Date"].dt.strftime("%d-%b-%y")

  top_growth = df2.groupby(df2["date_formatted"]).agg({
  'Views' : "max",
  'Video Likes Added' : "max",
  'Video Dislikes Added' : "min",
  'Video Likes Removed' : "min",
  'Average View Percentage' : "max",
  'Average Watch Time' : "max",
  'User Comments Added' : "max",
  'User Subscriptions Added' : "max",
  'User Subscriptions Removed' : "min"    
  }).reset_index().sort_values(by="User Subscriptions Added", ascending=False)
  return top_growth





def videos_decay():


  top_decay = df2.groupby(df2["date_formatted"]).agg({
  'Views' : "min",
  'Video Likes Added' : "min",
  'Video Dislikes Added' : "max",
  'Video Likes Removed' : "max",
  'Average View Percentage' : "min",
  'Average Watch Time' : "min",
  'User Comments Added' : "min",
  'User Subscriptions Added' : "min",
  'User Subscriptions Removed' : "max"    
  }).reset_index().sort_values(by="User Subscriptions Added", ascending=False).head(20)
  return top_decay


def videos_decay_no_head():

  top_decay = df2.groupby(df2["date_formatted"]).agg({
  'Views' : "min",
  'Video Likes Added' : "min",
  'Video Dislikes Added' : "max",
  'Video Likes Removed' : "max",
  'Average View Percentage' : "min",
  'Average Watch Time' : "min",
  'User Comments Added' : "min",
  'User Subscriptions Added' : "min",
  'User Subscriptions Removed' : "max"    
  }).reset_index().sort_values(by="User Subscriptions Added", ascending=False)
  return top_decay


top_by_country = df.groupby(df["Country Code"]).agg({
'Views' : "max",
'Video Likes Added' : "max",
'Video Dislikes Added' : "min",
'Video Likes Removed' : "min",
'Average View Percentage' : "max",
'Average Watch Time' : "max",
'User Comments Added' : "max",
'User Subscriptions Added' : "max",
'User Subscriptions Removed' : "min"    
}).reset_index().sort_values(by="User Subscriptions Added", ascending=False).head(500)




if __name__ == "__main__":
  top_core_audiences_by_views = (
      df.groupby("Country Code", as_index=False)["Views"]
        .sum()
        .sort_values(by="Views", ascending=False)
        .head(5)
  )
  top_core_audiences_by_views = top_core_audiences_by_views.drop(columns=["Views"])
  top_core_audiences_by_views


  top_core_audiences_by_views = df.groupby("Country Code")["Views"].sum().reset_index().sort_values(by="Views", ascending=False).head(5)
  top_core_audiences_by_views


# intrests of ken jee's audiences



top_core_aud_by_intrests = df.groupby("Video Title").agg({
'Is Subscribed' : "max",
'Views' : "max",
'Video Likes Added' : "max",
'Video Dislikes Added' : "min",
'Video Likes Removed' : "min",
'Average View Percentage' : "max",
'Average Watch Time' : "max",
'User Comments Added' : "max",
'User Subscriptions Added' : "max",
'User Subscriptions Removed' : "min"    
}).reset_index().sort_values(by="User Subscriptions Added", ascending=False).head(5)

def piechart_for_top_core_aud_by_intrests(top_core_aud_by_intrests):
  fig = px.pie(top_core_aud_by_intrests, values='Views', names='Video Title', title ="Top 5 biggest intrests of ken jee's audiences", color_discrete_sequence = px.colors.sequential.Magma)
  return fig
#conclusion 1 :the most popular ken jee's videos are "how i would learn data science ,if i had to start over", "satring over videos seem to be more popular"
#counclusion 2: people are looking for free data science courses


def scatterplot_for_top_core_aud_by_intrests(top_core_aud_by_intrests):
  fig = px.scatter(top_core_aud_by_intrests, x="Video Title", y="Views", color="Views",title = "Scatterplot for Top 5 biggest intrests of ken jee's audiences",
                  size='Views', hover_data=['Views',"Video Title"])
  return fig


def scatterplot_for_countries_with_most_subs(top_by_country):
  fig = px.line(top_by_country, x="User Subscriptions Added", y="Country Code", color="Country Code",title = "Countries with most subs to this channel", markers = True
                )
  return fig


def piecharts_for_countries_with_most_views(top_by_country):
  fig = px.pie(top_by_country, values='Views', names='Country Code', title =' piechart for Top Countries by core audiences', color_discrete_sequence = px.colors.sequential.Magma)
  return fig


#Conclusion to : What is the core audience and what are they intrested in?
#Conclusion: 1 : top core audience by "Views" :
#1 = "US with 285,593"
#2 = "INDIA with 203,055"
#3 = "UK with 49,982"
#4 = "CANADA with 49,982"
#5 = "Germany with  42,422"

#conclusion : 2 : top core audience by "Videos Likes added":
#1 = "US with 9165"
#2 = "INDIA with 8442"
#3 = "UK with 1589"
#4 = "CANADA with 1318"
#5 = "Germany with 1216"

#conclusion : 3 : top core audience by "Average view Percentag":
#1 = "UK with 921740455"
#2 = "GERMANY with 916349624"
#3 = "US with 9110105122"
#4 = "CANADA with 899897833"
#5 = "INDIA with 722197251"

#conclusion : 4 : top core audience by "Average Watch Time":
#1 = "CANADA with 873.361"
#2 = "UK with 757.451"
#3 = "US with 753.948"
#4 = "GERMANY with 700.364"
#5 = "INDIA with 475.984"

# what are the intrests of the core audiences?

#result 1:data science if started over
#result 2:best "free" data science courses "untold"
#result 3:"Data science projects for "beginners"
#Conclusion : Audiences are looking for fresh ways to learn data science from starting over as "most" are messed up in the "prosess",they are looking for "free ways" to learn and  need "beginner project ideas".
#Final Conclusion : These are the 3 biggest intrests of ken Jee's audiences.





# videos that have led to most growth
def videos_that_led_to_most_growth(df2):
  Videos_led_to_most_growth = df2.groupby("Video Title")["growth"].sum().reset_index().sort_values(by="growth", ascending=False).head(5)
  Videos_led_to_most_growth
# these videos have led to the most growth

if __name__ == "__main__":
  df2["growth"] = (df2["User Subscriptions Added"] - df2["User Subscriptions Removed"]) - (df2["Video Likes Added"] - df2["Video Likes Added"])+(df2["Views"])
  df2["growth"]




