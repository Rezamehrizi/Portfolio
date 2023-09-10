import requests
import csv

API_KEY = 'YOUR_API_KEY'
BASE_URL = '<https://www.googleapis.com/youtube/v3/search>'

search_keywords = 'artificial+intelligence'
params = {
    'part': 'snippet',  # Retrieve basic video information
    'q': search_keywords,  # Search term
    'maxResults': 1000,  # Number of results per page
    'key': API_KEY  # Your API key
}

response = requests.get(BASE_URL, params=params)
data = response.json()


# Process the response
for item in data['items']:
    video_id = item['id']['videoId']
    video_title = item['snippet']['title']
    published_at = item['snippet']['publishedAt']

    # Fetch additional video details using the video ID
    video_details_url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics,snippet&id={video_id}&key={API_KEY}"
    video_details_response = requests.get(video_details_url)
    video_details_data = video_details_response.json()

    video_info = video_details_data['items'][0]
    print(video_info)
    # Extract relevant information
    video_duration = video_info['contentDetails']['duration']
    like_count = video_info['statistics'].get('likeCount', 0)
    dislike_count = video_info['statistics'].get('dislikeCount', 0)
    comment_count = video_info['statistics'].get('commentCount', 0)
    tags = video_info['snippet'].get('tags', [])
    channel_title = video_info['snippet']['channelTitle']
    category = video_info['snippet'].get('categoryId', '')
    thumbnails = video_info['snippet']['thumbnails']
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    video_data = {
        'title': video_title,
        'video_id': video_id,
        'published_at': published_at,
        'duration': video_duration,
        'like_count': like_count,
        'dislike_count': dislike_count,
        'comment_count': comment_count,
        'tags': tags,
        'channel_title': channel_title,
        'category': category,
        'thumbnails': thumbnails,
        'video_url': video_url
    }

    all_video_details.append(video_data)
# print(all_video_details)


# Specify the CSV file path
csv_file_path = 'youtube_videos.csv'

# Save video details to the CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'video_id', 'published_at', 'duration', 'like_count', 'dislike_count', 'comment_count', 'tags', 'channel_title', 'category', 'thumbnails', 'video_url']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # Write header row

    for video_data in all_video_details:
        writer.writerow(video_data)

print("CSV file saved:", csv_file_path)


import sqlite3  # Import the SQLite library

# Initialize the SQLite database connection
conn = sqlite3.connect('youtube_videos.db')  # Create or connect to the database
cursor = conn.cursor()  # Create a cursor object

# Create a table to store the YouTube video data
cursor.execute('''
    CREATE TABLE IF NOT EXISTS youtube_videos (
        id INTEGER PRIMARY KEY,
        title TEXT,
        video_id TEXT,
        published_at TEXT,
        duration TEXT,
        like_count INTEGER,
        dislike_count INTEGER,
        comment_count INTEGER,
        tags TEXT,
        channel_title TEXT,
        category TEXT,
        thumbnails TEXT,
        video_url TEXT
    )
''')

# Process the response and save data to the database
for item in data['items']:
    # Your existing code to extract video information...

    # Insert data into the database
    cursor.execute('''
        INSERT INTO youtube_videos (
            title, video_id, published_at, duration, like_count, dislike_count, 
            comment_count, tags, channel_title, category, thumbnails, video_url
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        video_title, video_id, published_at, video_duration, like_count,
        dislike_count, comment_count, ', '.join(tags), channel_title, category,
        str(thumbnails), video_url
    ))

# Commit the changes and close the database connection
conn.commit()
conn.close()



# Data analysis



#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np


# In[47]:


youtube_videos_processed = pd.read_csv('youtube_videos_processed.csv')


# ## Engagement Analysis

# ### Determine the most popular video categories based on the "category_name" column.
# 

# In[164]:


import plotly.express as px
import plotly.io as pio


# Load your dataset
youtube_videos_processed = pd.read_csv('youtube_videos_processed.csv')

# Group and aggregate data
category_counts = youtube_videos_processed['category_name'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

# Create an interactive bar plot
fig = px.bar(category_counts, x='Category', y='Count', color='Category',
             labels={'Category': 'Video Category', 'Count': 'Number of Videos'},
             title='Popular Video Categories')

# Customize the appearance of the plot
fig.update_layout(xaxis_tickangle=-45)

# Show the interactive plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='engagement-category-video-numbers.html', auto_open=False, include_plotlyjs='cdn')


# ### Calculate the average number of likes and comments for videos in each category.
# 

# In[165]:



# Group the data by 'category_name' and calculate the mean for 'like_count' and 'comment_count'
category_likes_comments_avg = youtube_videos_processed.groupby('category_name')[['like_count', 'comment_count']].mean().reset_index()

# Create an interactive bar plot
fig = px.bar(category_likes_comments_avg, x='category_name', y=['like_count', 'comment_count'],
             labels={'like_count': 'Average Likes', 'comment_count': 'Average Comments'},
            color_discrete_sequence=['darkcyan', 'chocolate'], 
             title='Average Likes and Comments by Video Category')

# Customize the layout
fig.update_xaxes(tickangle=45)
fig.update_layout(xaxis_title='Video Category', yaxis_title='Average Count')

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='engagement-category-likes-comments.html', auto_open=False, include_plotlyjs='cdn')


# ### Do videos published on specific days or months tend to get more engagement

# Days

# In[166]:



# Convert the "published_at" column to datetime
youtube_videos_processed['published_at'] = pd.to_datetime(youtube_videos_processed['published_at'])

# Extract the day of the week from the "published_at" column
youtube_videos_processed['day_of_week'] = youtube_videos_processed['published_at'].dt.day_name()

# Specify the desired order of days of the week
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Group the data by day of the week and calculate the average engagement
engagement_by_day = youtube_videos_processed.groupby('day_of_week')['like_count', 'comment_count'].mean().reset_index()

# Calculate the total engagement as the sum of likes and comments
engagement_by_day['total_engagement'] = engagement_by_day['like_count'] + engagement_by_day['comment_count']

# Create a bar plot to visualize the correlation
fig = px.bar(
    engagement_by_day,
    x='day_of_week',
    y='total_engagement',
    title='Average Engagement by Day of the Week',
    labels={'day_of_week': 'Day of the Week', 'total_engagement': 'Average Engagement'},
    color_discrete_sequence=['cadetblue'],  # Set the color to olive
    category_orders={"day_of_week": day_order}  # Set the desired order
)

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='engagement-days.html', auto_open=False, include_plotlyjs='cdn')


# Months

# In[167]:



# Extract the month from the "published_at" column
youtube_videos_processed['month'] = youtube_videos_processed['published_at'].dt.month_name()

# Define the order of months
month_order = list(calendar.month_name)[1:]  # Get month names in order

# Group the data by month and calculate the average engagement
engagement_by_month = youtube_videos_processed.groupby('month')['like_count', 'comment_count'].mean().reset_index()

# Calculate the total engagement as the sum of likes and comments
engagement_by_month['total_engagement'] = engagement_by_month['like_count'] + engagement_by_month['comment_count']

# Sort the data by month order
engagement_by_month['month'] = pd.Categorical(engagement_by_month['month'], categories=month_order, ordered=True)
engagement_by_month = engagement_by_month.sort_values('month')

# Create a bar plot to visualize the correlation
fig = px.bar(
    engagement_by_month,
    x='month',
    y='total_engagement',
    title='Average Engagement by Month',
    labels={'month': 'Month', 'total_engagement': 'Average Engagement'},
    color_discrete_sequence=['darkkhaki'],
)

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='engagement-months.html', auto_open=False, include_plotlyjs='cdn')


# Years

# In[168]:


# Extract the year from the "published_at" column
youtube_videos_processed['year'] = youtube_videos_processed['published_at'].dt.year

# Group the data by year and calculate the average engagement
engagement_by_year = youtube_videos_processed.groupby('year')['like_count', 'comment_count'].mean().reset_index()

# Calculate the total engagement as the sum of likes and comments
engagement_by_year['total_engagement'] = engagement_by_year['like_count'] + engagement_by_year['comment_count']

# Create a bar plot to visualize the correlation
fig = px.bar(
    engagement_by_year,
    x='year',
    y='total_engagement',
    title='Average Engagement by Year',
    labels={'year': 'Year', 'total_engagement': 'Average Engagement'},
    color_discrete_sequence=['steelblue'],
)

# Show all years on the x-axis
fig.update_xaxes(tickmode='linear', tick0=engagement_by_year['year'].min(), dtick=1)

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='engagement-years.html', auto_open=False, include_plotlyjs='cdn')


# In[110]:



# ## Duration Analysis

# ### Analyze if there's a relationship between video duration (in minutes) and engagement

# In[169]:


import plotly.graph_objects as go
import statsmodels.api as sm

# Calculate engagement column
youtube_videos_processed['engagement'] = youtube_videos_processed['like_count'] + youtube_videos_processed['comment_count']

# Filter out records with duration greater than 200 minutes
filtered_data = youtube_videos_processed[(youtube_videos_processed['duration_minutes'] <= 240) & (youtube_videos_processed['engagement'] < 2e6)]
# filtered_data = youtube_videos_processed[youtube_videos_processed['duration_minutes'] <= 120]

# Define a function to fit a kernel regression
def kernel_regression(x, y, bandwidth=1.0):
    # Create a lowess kernel regression model
    lowess = sm.nonparametric.lowess
    result = lowess(y, x, frac=1/bandwidth)
    return result[:, 1]

# Fit kernel regression for comments
engagement_smoothed = kernel_regression(filtered_data['duration_minutes'], filtered_data['engagement'])

# Create a scatter plot for video duration vs. number of comments along with kernel regression curves
fig = px.scatter(
    filtered_data,
    x='duration_minutes',
    y='engagement',
    title='Video Duration vs. Number of Engagements',
    labels={'duration_minutes': 'Duration (minutes)', 'engagement': 'Number of Engagements'},
    opacity=0.6,
    size='engagement',  # Set the size based on engagement values
    size_max=30  # Adjust the maximum marker size as needed
)

fig.show()

# Save the intercative plot
pio.write_html(fig, file='duration-engagement-scatter.html', auto_open=False, include_plotlyjs='cdn')


# In[ ]:





# ### Calculate the average duration of videos in different categories

# In[170]:


# Group the data by category_name and calculate the average duration for each category
average_duration_by_category = youtube_videos_processed.groupby('category_name')['duration_minutes'].mean().reset_index()

# Create a bar plot using Plotly
fig = px.bar(
    average_duration_by_category,
    x='category_name',
    y='duration_minutes',
    title='Average Duration of Videos by Category',
    labels={'duration_minutes': 'Average Duration (minutes)'},
    color='category_name',  # Use different colors for each category bar
)

# Customize the layout of the plot
fig.update_layout(
    xaxis_title='Category',
    yaxis_title='Average Duration (minutes)',
    xaxis={'categoryorder': 'total descending'},  # Sort the categories by total duration in descending order
)

# Add data labels to the bars
fig.update_traces(texttemplate='%{y:.2f}', textposition='outside')

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='duration-category.html', auto_open=False, include_plotlyjs='cdn')


# ### Calculate the average duration of videos published in each month or year

# In[171]:


import calendar

# Extract the month and year from the "published_at" column
youtube_videos_processed['month'] = youtube_videos_processed['published_at'].dt.month_name()
youtube_videos_processed['year'] = youtube_videos_processed['published_at'].dt.year

# Group the data by month and calculate the average video duration
average_duration_by_month = youtube_videos_processed.groupby('month')['duration_minutes'].mean().reset_index()

# Sort the data by the order of months
month_order = list(calendar.month_name)[1:]  # Get month names in order
average_duration_by_month['month'] = pd.Categorical(average_duration_by_month['month'], categories=month_order, ordered=True)
average_duration_by_month = average_duration_by_month.sort_values('month')

# Create a bar plot to visualize the average duration by month
fig = px.bar(
    average_duration_by_month,
    x='month',
    y='duration_minutes',
    title='Average Video Duration by Month',
    labels={'month': 'Month', 'duration_minutes': 'Average Duration (minutes)'},
    color_discrete_sequence=['darkgoldenrod'],
)

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='duration-months.html', auto_open=False, include_plotlyjs='cdn')

# Group the data by year and calculate the average video duration
average_duration_by_year = youtube_videos_processed.groupby('year')['duration_minutes'].mean().reset_index()

# Create a bar plot to visualize the average duration by year
fig = px.bar(
    average_duration_by_year,
    x='year',
    y='duration_minutes',
    title='Average Video Duration by Year',
    labels={'year': 'Year', 'duration_minutes': 'Average Duration (minutes)'},
    color_discrete_sequence=['chocolate'],
)

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='duration-years.html', auto_open=False, include_plotlyjs='cdn')


# ### Determine if there's a trend in the number of videos published each year.

# In[172]:



# Group the data by year and count the number of videos published each year
videos_published_by_year = youtube_videos_processed.groupby('year').size().reset_index(name='count')

# Create a line plot to visualize the trend in the number of videos published each year
fig = px.line(
    videos_published_by_year,
    x='year',
    y='count',
    title='Trend in Number of Videos Published Each Year',
    labels={'year': 'Year', 'count': 'Number of Videos Published'},
    markers=True,  # Show markers on data points
)

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='video-numbers-year.html', auto_open=False, include_plotlyjs='cdn')


# ### Analyze whether video engagement metrics have changed over the years.

# In[174]:



# Group the data by year and calculate the average likes and comments for each year
engagement_over_time = youtube_videos_processed.groupby('year').agg({'engagement': 'mean'}).reset_index()

# Create a line plot to visualize the change in average likes over the years
fig = px.line(
    engagement_over_time,
    x='year',
    y='engagement',
    title='Change in Average Engagement Over the Years',
    labels={'year': 'Year', 'engagement': 'Average Engagements'},
    markers=True,  # Show markers on data points
)

# Show the plots
fig.show()

# Save the intercative plot
pio.write_html(fig, file='engagement-year-line.html', auto_open=False, include_plotlyjs='cdn')


# ## Text Analysis

# ### Perform sentiment analysis on video titles. Are positive or negative titles more engaging?

# In[175]:


from textblob import TextBlob

# Function to perform sentiment analysis and return labels
def get_sentiment(text):
    analysis = TextBlob(text)
    
    # Define the sentiment labels
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

# Apply sentiment analysis to the 'title' column and create a new column 'sentiment'
youtube_videos_processed['sentiment'] = youtube_videos_processed['title'].apply(get_sentiment)


# In[176]:




# Calculate the engagement score for each video
youtube_videos_processed['engagement'] = youtube_videos_processed['like_count'] + youtube_videos_processed['comment_count']

# Group the data by 'sentiment' and calculate the average engagement score
sentiment_engagement = youtube_videos_processed.groupby('sentiment')['engagement'].mean().reset_index()

# Sort the DataFrame by average engagement score in descending order
sentiment_engagement = sentiment_engagement.sort_values(by='engagement', ascending=False)


# Create a bar plot using Plotly
fig = px.bar(
    sentiment_engagement,
    x='sentiment',
    y='engagement',
    title='Average Engagement Score by Sentiment',
    labels={'sentiment': 'Sentiment', 'engagement': 'Average Engagement Score'},
    color='sentiment',  # Use different colors for each sentiment
)

# Sort the bars in descending order
fig.update_xaxes(categoryorder='total descending')

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='sentiment-engagement.html', auto_open=False, include_plotlyjs='cdn')


# ### Analyze the most common words or phrases in video titles

# In[177]:


import nltk
from nltk.corpus import stopwords
from wordcloud import WordCloud  # You'll need the wordcloud library for this
import re

# Download NLTK stopwords if not already downloaded
nltk.download('stopwords')

# Define a function to clean the text and remove symbols
def clean_text(text):
    # Remove symbols and special characters
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    return cleaned_text

# Apply the clean_text function to your video titles
youtube_videos_processed['cleaned_title'] = youtube_videos_processed['title'].apply(clean_text)

# Combine all titles into a single string
titles = " ".join(youtube_videos_processed['cleaned_title'])

# Convert the text to lowercase and split it into words
words = titles.lower().split()

# Remove common stopwords (e.g., 'the', 'and', 'is') from the list of words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Create a Word Cloud
wordcloud = WordCloud(width=1600, height=800, max_words=100, background_color='white').generate(" ".join(filtered_words))

# Create a figure for the Word Cloud
fig = px.imshow(wordcloud, color_continuous_scale='Viridis')

# Hide axis labels and ticks for a cleaner appearance
fig.update_xaxes(showticklabels=False)
fig.update_yaxes(showticklabels=False)

# Show the Word Cloud
fig.show()

# Save the intercative plot
pio.write_html(fig, file='sentiment-wordcloud.html', auto_open=False, include_plotlyjs='cdn')



# In[179]:


from collections import Counter

# Convert the text to lowercase and split it into words
words = titles.lower().split()

# Remove common stopwords (e.g., 'the', 'and', 'is') from the list of words
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word not in stop_words]

# Calculate word frequencies
word_freq = Counter(filtered_words)

# Create a DataFrame from the word frequencies
word_freq_df = pd.DataFrame(word_freq.items(), columns=['Word', 'Frequency'])

# Sort the DataFrame by frequency in descending order
word_freq_df = word_freq_df.sort_values(by='Frequency', ascending=False)

# Select the top N most common words/phrases to display
top_n = 20  # You can adjust this value as needed
top_words = word_freq_df.head(top_n)

# Create a bar plot using Plotly
fig = px.bar(
    top_words,
    y='Frequency',
    x='Word',
    title='Most Common Words/Phrases in Video Titles',
    labels={'Frequency': 'Frequency', 'Word': 'Word/Phrase'},
    orientation='v',  # Horizontal bar plot
)

# Show the plot
fig.show()

# Save the intercative plot
pio.write_html(fig, file='sentiment-word-bar.html', auto_open=False, include_plotlyjs='cdn')


# 
