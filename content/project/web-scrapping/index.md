---
title: Web Scraping Insights from AI Related YouTube Videos
summary: This project scrapes detailed data from AI-related videos on YouTube and offers visualization insights based on the collected information.
tags:
- Data Science
- Web Scraping
- SQL
- Sentiment Analysis
- Deep Learning
date: "2023-08-28"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
#caption: Photo by DataSciMT on GitHub
  focal_point: Smart


links:
- icon: file-alt
  icon_pack: fas
  name: Python Code
  url: uploads/webscraping-analysis.py
  # link: uploads/Web-Scraping.py

- icon: file-alt
  icon_pack: fas
  name: SQL Code
  url: uploads/data-processing.sql
  # link: uploads/Web-Scraping.py

- icon: file-alt
  icon_pack: fas
  name: Dataset (CSV)
  url: uploads/youtube_videos.csv
  # link: uploads/youtube_videos.csv

- icon: file-alt
  icon_pack: fas
  name: Processed Dataset (SQL)
  url: uploads/youtube_videos_processed.csv
  # link: uploads/youtube_videos.csv

url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---
<style>
body {
text-align: justify}
</style>

The impact of AI has been growing rapidly, with the introduction of ChatGPT being a significant contributor to this trend. As we look ahead, the AI landscape is poised for exciting and transformative changes. Hence, in this project, my focus will be on gathering data from YouTube videos related to Artificial Intelligence (AI). The project involves three main tasks as follows:
1. [**YouTube Videos Web Scrapping:**](#web-scrapping-youtube-videos-dataset) I'll craft a Python script designed to tap into the YouTube API, allowing me to extract information from videos tied to the AI theme.
2. [**Pre-processing Videos Dataset**](#data-processing-using-sql) Once I've got the data in hand, I'll smoothly slide it into a pandas data frame for better organization. 

3. [**Descriptive Analysis of Videos Dataset:**](#descriptive-analysis) My next steps involve diving into analysis and visualizations, keeping things simple with the helpful Plotly Python library.


![ideogram-webscraping](ideogram-webscraping.JPEG)
###  Web Scrapping YouTube Videos Dataset

To kick things off, I'll go through the process of generating YouTube API key. Once that's in place, I'll navigate through Google's detailed YouTube API documentation to access various YouTube data. With that, I'll move on to crafting the Python code that forms the foundation of this section.


**API Key from Google:** The first step involves creating a Google API key. I start by visiting the [Google Developer Console](https://console.cloud.google.com/cloud-resource-manager?pli=1) through my browser. Once there, I sign in using my Google account. Upon signing in, I click the "Create a Project" button. Creating a project is a priority here, and I have options: I can either click the button or go to "Select a Project" at the top. Now, I create a fresh project, named "YouTube Analysis Project" and hit "Create". Giving it a few seconds to come to life. Next, it's time to enable the API. In the Library, I search for the API I'm aiming for – in this case, the YouTube Data API. I give it the green light by clicking "Enable." Now, onto the final touch: crafting my API key. I slide over to the "Credentials" section on the left side and click "Create Credential." For my project, I'm sticking with an API key – no need for the OAuth client ID. 



**Make API Requests:** After I obtained my API key, I used it to authenticate my requests to the YouTube Data API. This key acted like my digital pass that let the API know I was authorized to access its resources. The YouTube Data API has various "endpoints" that correspond to different types of data or actions. For my project, I focused on the "search" endpoint, which allowed me to find videos based on specific search criteria. I constructed a request to this endpoint, specifying parameters like my API key and the search query "Artificial Intelligence" and "AI".



**Request Parameters:** API requests can be personalized by adding parameters. These parameters helped me tailor my request to my specific needs. For instance, I adjusted the number of results per page by setting the "maxResults" parameter. These parameters gave me flexibility in how I retrieved the data.

```python
search_keywords = 'Artificial+Intelligence'+'AI'
params = {
    'part': 'snippet',  # Retrieve basic video information
    'q': 'artificial intelligence',  # Search term
    'maxResults': 1000,  # Number of results per page
    'key': API_KEY  # Your API key
}
```

The provided code snippet is setting up parameters for making a search request to the YouTube Data API. `params = {...}` is a Python dictionary that stores the parameters needed for the API request. Here is the breakdown for this dictionary:

- `'part': 'snippet'`: This parameter specifies that we want to retrieve basic information about the videos, like their titles, descriptions, and thumbnails. The `'snippet'` part is required in most API requests.
- `'q': 'search_keywords'`: This is the search term I’m looking for on YouTube. In this case, it's `search_keywords = 'Artificial+Intelligence'+'AI'`.
- `'maxResults': 1000`: This parameter indicates the maximum number of results I want per page. The value `1000` suggests you want to retrieve up to 1000 videos per page of the search results.
- `'key': API_KEY`: This is where I would insert my actual YouTube Data API key. The API key serves as my authentication to access the API.

So, all together, this code is preparing the parameters for a YouTube Data API search request. It's set up to search for videos related to "artificial intelligence" and "AI," retrieve basic information about those videos (like titles and descriptions), and return up to 1000 results per page. The `API_KEY` should be replaced with my actual YouTube Data API key for proper authentication.

**Parsing API Responses:** When I made a request to the API, it responded with data in JSON format. JSON is a structured way of representing data that's easy for both humans and machines to understand. My task was to parse (read and interpret) this JSON response.

```python
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'
response = requests.get(BASE_URL, params=params)
data = response.json()
```
```python
search_keywords = 'Artificial+Intelligence'+'AI'
params = {
    'part': 'snippet',  # Retrieve basic video information
    'q': 'artificial intelligence',  # Search term
    'maxResults': 1000,  # Number of results per page
    'key': API_KEY  # My API key
}
```
 The response included an array called "items," where each item corresponded to a video.

**Extract Information:** Within each video item, a treasure trove of information was waiting. This included details like the video's title, unique ID, upload date, and view count. I went through each item in the JSON response, extracting the specific pieces of information that were relevant to my project.


**Process the Response:** I process the response from the YouTube Data API in order to extract and gather valuable information about the videos. For each video item in the API response, I perform the following steps:

<details>
<summary style="color: green;">Click to reveal code</summary>

```python
for item in data['items']:
    video_id = item['id']['videoId']
    video_title = item['snippet']['title']
    published_at = item['snippet']['publishedAt']

    # Fetch additional video details using the video ID
    video_details_url = f"https://www.googleapis.com/youtube/v3/videos?part=contentDetails,statistics,snippet&id={video_id}&key={API_KEY}"
    video_details_response = requests.get(video_details_url)
    video_details_data = video_details_response.json()

    video_info = video_details_data['items'][0]

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

    # Create a dictionary to store video details
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

    # Append video data to the list
    all_video_details.append(video_data)
```
</details>

Finally, I save the extracted video data into a CSV and SQL files.

<details>
<summary style="color: green;">Click to reveal code</summary>

```python
# Specify the CSV file path
csv_file_path = 'youtube_videos.csv'

# Save video details to the CSV file
with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
    fieldnames = ['title', 'video_id', 'published_at', 'duration', 'like_count', 'dislike_count', 'comment_count', 'tags', 'channel_title', 'category', 'thumbnails', 'video_url']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()  # Write header row

    for video_data in all_video_details:
        writer.writerow(video_data)


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

```
</details>


This entire process allows me to efficiently process the API responses, extract relevant video details, and store them in a structured CSV file.


![ideogram-processing](ideogram-processing.JPEG)
### Processing YouTube Video Dataset Using SQL

To prepare the data for further analysis, I will perform the following data processing steps. The data is stored in a database called `youtube_videos` and I will create an SQL script to improve the `youtube_videos` table by adding new columns and filling them with relevant data extracted from existing columns. This makes the data more informative and readable.  
1. **Dropping thumbnails Column:** I will first remove the `thumbnails` column from the data set, as it is not needed.

    ```sql
    -- Remove the 'thumbnails' column from the youtube_videos table
    ALTER TABLE youtube_videos
    DROP COLUMN thumbnails;
    ```
   

2. **Creating Columns for Year and Month:** Two new columns, `year` and `month`, are added to the `youtube_videos` table. These columns will be used to store the year and month information extracted from the `published_at` column. This code updates the newly added `year` and `month` columns by extracting the corresponding values from the `published_at` column, assuming that the `published_at` column contains dates in the format 'YYYY-MM-DD'.

   ```sql
   -- Add 'year' and 'month' columns to store publication date information
    ALTER TABLE youtube_videos
    ADD year INT, month INT;

    -- Update the 'year' and 'month' columns based on the 'published_at' column
    UPDATE youtube_videos
    SET
        year =  SUBSTRING(published_at, 1, 4),   -- Extract the year part (e.g., '2023' from '2023-09-10')
        month = SUBSTRING(published_at, 6, 2);  -- Extract the month part (e.g., '09' from '2023-09-10');

   ```
  

4. **Creating a Column for Duration in Minutes:**
A new column, `duration_minutes` is added to the table to store the duration of videos in minutes. This part of the code calculates the duration of videos in minutes and updates the `duration_minutes` column based on the information in the `duration` column, which is expected to be in the format 'PT#H#M' (e.g., 'PT5M' for 5 minutes).
<details>
<summary style="color: green;">Click to reveal code</summary>

   ```sql
   -- Add a new column 'duration_minutes' to store video duration in minutes
    ALTER TABLE youtube_videos
    ADD duration_minutes INT;

    -- Update 'duration_minutes' based on the 'duration' column (format: 'PT#H#M')
    UPDATE youtube_videos
    SET
        duration_minutes = 
            CASE 
                WHEN CHARINDEX('H', duration) > 0 THEN 
                    CASE 
                        WHEN CHARINDEX('M', duration) > 0 THEN
                            -- Calculate duration in minutes for 'HH:MM' format (e.g., '1H25M' becomes 85 minutes)
                            CAST(SUBSTRING(duration, CHARINDEX('H', duration) + 1, CHARINDEX('M', duration) - CHARINDEX('H', duration) - 1) AS INT) + 
                            CAST(SUBSTRING(duration, 3, CHARINDEX('H', duration) - 3) AS INT) * 60
                        ELSE
                            -- Calculate duration in minutes for 'HH' format (e.g., '1H' becomes 60 minutes)
                            CAST(SUBSTRING(duration, 3, CHARINDEX('H', duration) - 3) AS INT) * 60
                    END
                WHEN CHARINDEX('M', duration) > 0 THEN
                    -- Extract duration in minutes for 'MM' format (e.g., '25M' becomes 25 minutes)
                    CAST(SUBSTRING(duration, 3, CHARINDEX('M', duration) - 3) AS INT)
                ELSE
                    0 -- Handle cases with no 'H' or 'M' (e.g., "PT52S")
            END;
  ```
  </details>
      

4. **Creating a Column for Category Name:** A new column, `category_name`, is added to store the category names of videos. This code updates the `category_name` column based on the `category` column. It assigns human-readable category names to each video based on the [category code](#https://developers.google.com/youtube/v3/docs/videoCategories/list).

<details>
<summary style="color: green;">Click to reveal code</summary>

```sql
-- Add the category_name column to youtube_videos
ALTER TABLE youtube_videos
ADD category_name NVARCHAR(255); -- Adjust the data type and length as needed

-- Update the category_name column based on the category code
UPDATE youtube_videos
SET category_name =
    CASE
        WHEN category = '1' THEN 'Film & Animation'
        WHEN category = '2' THEN 'Autos & Vehicles'
        WHEN category = '10' THEN 'Music'
        WHEN category = '15' THEN 'Pets & Animals'
        WHEN category = '17' THEN 'Sports'
        WHEN category = '18' THEN 'Short Movies'
        WHEN category = '19' THEN 'Travel & Events'
        WHEN category = '20' THEN 'Gaming'
        WHEN category = '21' THEN 'Videoblogging'
        WHEN category = '22' THEN 'People & Blogs'
        WHEN category = '23' THEN 'Comedy'
        WHEN category = '24' THEN 'Entertainment'
        WHEN category = '25' THEN 'News & Politics'
        WHEN category = '26' THEN 'Howto & Style'
        WHEN category = '27' THEN 'Education'
        WHEN category = '28' THEN 'Science & Technology'
        WHEN category = '29' THEN 'Nonprofits & Activism'
        WHEN category = '30' THEN 'Movies'
        WHEN category = '31' THEN 'Anime/Animation'
        WHEN category = '32' THEN 'Action/Adventure'
        WHEN category = '33' THEN 'Classics'
        WHEN category = '34' THEN 'Comedy'
        WHEN category = '35' THEN 'Documentary'
        WHEN category = '36' THEN 'Drama'
        WHEN category = '37' THEN 'Family'
        WHEN category = '38' THEN 'Foreign'
        WHEN category = '39' THEN 'Horror'
        WHEN category = '40' THEN 'Sci-Fi/Fantasy'
        WHEN category = '41' THEN 'Thriller'
        WHEN category = '42' THEN 'Shorts'
        WHEN category = '43' THEN 'Shows'
        WHEN category = '44' THEN 'Trailers'
        ELSE 'Unknown'
    END;

   
```
</details>


Finally, I stored the processed data set to a CSV file for conducting descrptive analysis in Python.


![ideogram-analysis](ideogram-analysis.JPEG)
### Descriptive Analysis of YouTube Video Dataset

After conducting an initial data cleaning process using SQL, I will be performing a through analysis, splitting it into three parts as follows:

- [**Engagement Analysis:**](#engagement-analysis) This part focuses on how viewers interact with YouTube videos. I examine which video categories are most popular, what are the average of likes and comments count for each category, and how video publication affects engagement.

- [**Duration Analysis:**](#duration-analysis) The second part explores the connection between video length and user engagement, revealing the ideal video durations.

- [**Text Analysis:**](#text-analysis) The third part uncovers the secrets of video titles. We analyze the most frequent words and phrases in video titles and determine whether positive or negative titles tend to draw more viewers. 

These three analytical sections together provide a holistic view of what makes YouTube videos successful, from viewer behavior and video length to the power of titles.

#### Engagement Analysis:
In this section, I looked deeper into the YouTube dataset, aiming to answer the key questions regarding what engages online viewers. The followings are three questions in this regard:

*1. Determine the most published video categories based on the "category_name" column?*

By grouping the videos according to their categories using the "category_name" column, I can calculate the total number of videos published for each category. This helps me to order the categories based on their number of published videos and find out which ones are more popular.

<!-- Embed the Plotly plot using an iframe -->
<iframe src="engagement-category-video-numbers.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the distribution of videos across different categories on a video sharing platform. It suggests that the platform users are more interested in topics related to current affairs, learning, and innovation, as these categories have the highest number of videos. On the other hand, categories such as sports, gaming, and film & animation have fewer videos, indicating that they are less popular or less frequently uploaded. The graph also reveals the diversity of content available on the platform, as it covers a wide range of genres and interests.


<!-- Embed the Plotly plot using an iframe -->
<iframe src="engagement-year-line.html" width="800" height="600" frameborder="0"></iframe>

The line graph shows the trend in the number of videos published each year from 2012 to 2022. It indicates that the video publishing activity has increased steadily over the years, with a significant jump from 2020 to 2022. This could suggest that the video sharing platform has gained more popularity and users in recent years, or that the users have become more active and creative in producing and uploading videos. The graph also shows the growth potential of the platform, as the number of videos published has not reached a plateau yet.


*2. Calculate the average number of likes and comments for videos in each category?*

I also calculate the average number of likes and comments per video for each category to measure the level of engagement. This helps us identify which categories generate more interactions and feedback from viewers. 

<!-- Embed the Plotly plot using an iframe -->
<iframe src="engagement-category-likes-comments.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the average number of likes and comments for different video categories. It suggests that the videos in the "Comedy" and "Science & Technology" categories are more engaging and appealing to the viewers, as they receive more likes and comments than other categories. On the other hand, the videos in the "News & Politics" and "Sports" categories are less interactive and attractive, as they receive fewer likes and comments. The graph also reveals the preferences and tastes of the viewers, as they seem to enjoy humorous and informative content more than other types of content.


*3. Analyze how video publication dates correlate with engagement. Do videos published on specific days or months tend to get more engagement?* 

Furthermore, I analyze how video publication dates affect engagement. I investigate whether videos published on certain days of the week or months of the year tend to get more likes and comments. This enables us to discover any seasonal or temporal patterns in viewer behavior and preferences.

<!-- Embed the Plotly plot using an iframe -->
<iframe src="engagement-months.html" width="800" height="600" frameborder="0"></iframe>
Hello, this is Bing. Based on the image description, here is a possible interpretation of the result:

The bar graph shows the average engagement by month. It indicates that the engagement varies throughout the year, with a peak in December and a dip in March. This could suggest that the engagement is influenced by seasonal factors, such as holidays, weather, or events. For example, December might have higher engagement because of Christmas, New Year, or winter break. March might have lower engagement because of spring break, exams, or less activity. The graph also shows the potential for increasing engagement in other months by creating more relevant and appealing content.

<iframe src="engagement-years.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the average engagement by year from 2012 to 2023. It suggests that the engagement has been declining over time, with a sharp drop from 2016 to 2022. This could indicate that the platform or the content has lost its appeal or relevance to the viewers, or that there is more competition or saturation in the market. The graph also shows the challenge of maintaining or increasing engagement in the future, as the projected value for 2023 is lower than the previous years.

<details>
<summary style="color: green;">Click to reveal code</summary>

```python
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

   
```
</details>

#### Duration Analysis:

For this analysis, I aim to understand the role of video duration in YouTube content. I use the 'video_duration' column to measure the length of videos and then compare it with the 'engagement' column, which is calculated as the sum of likes, and comments. This allows me to answer the following questions:

*1. Analyze whether there's a correlation between video duration and engagement:* 

This allows me to see if longer or shorter videos tend to get more interaction from viewers.

<!-- Embed the Plotly plot using an iframe -->
<iframe src="duration-engagement-scatter.html" width="800" height="600" frameborder="0"></iframe>

The scatter plot shows the relationship between video duration and number of engagements. It implies that there is a negative correlation between the two variables, meaning that videos with shorter durations tend to have more engagements than videos with longer durations. This could suggest that the viewers have a short attention span or prefer concise and fast-paced content. The plot also shows some exceptions, where videos with longer durations have high number of engagements. These could be videos that are very captivating, informative, or entertaining.


*2. Calculate the average duration of videos in different categories?*

I also calculate the 'Average duration of videos in different categories' by grouping the videos by their 'category_name' column. This helps me identify the typical length of videos in various genres and how they differ from each other. 

<!-- Embed the Plotly plot using an iframe -->
<iframe src="duration-category.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the average duration of videos by category. It indicates that the videos in the Education category are the longest, while the videos in the Science & Technology category are the shortest. This could reflect the different purposes and formats of the videos in each category. For example, the Education videos might be longer because they aim to teach or explain complex topics, while the Science & Technology videos might be shorter because they showcase or demonstrate innovations or discoveries. The graph also shows the diversity and variety of the video content available.


*3. Calculate the average duration of videos published in each month or year?* 

Furthermore, I calculate the 'Average duration of videos published in each month or year' by extracting the month and year from the 'published_at' column. This enables me to discover any trends or patterns in video length over time and how they relate to viewer preferences. This analysis takes me through the complex relationship between video duration, categories, and publication trends, offering a holistic view of the YouTube landscape.

<!-- Embed the Plotly plot using an iframe -->
<iframe src="duration-months.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the average video duration by month. It suggests that the video duration varies throughout the year, with a peak in July and a dip in December. This could imply that the video creators or the viewers have different preferences or behaviors depending on the season. For example, July might have longer videos because of summer break, vacation, or leisure time. December might have shorter videos because of holidays, family gatherings, or busy schedules. The graph also shows the potential for optimizing video duration in different months to increase engagement.

<iframe src="duration-years.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the average video duration by year. It indicates that the video duration has changed over time, with an increasing trend from 2012 to 2018, and a decreasing trend from 2020 to 2022. This could reflect the evolution of the video content, the platform, or the audience. For example, 2018 might have longer videos because of more in-depth or complex topics, more interactive or live features, or more loyal or engaged viewers. 2022 might have shorter videos because of more concise or simple topics, more short-form or ephemeral features, or more casual or diverse viewers. The graph also shows the challenge of adapting to the changing preferences and expectations of the video market.

<details>
<summary style="color: green;">Click to reveal code</summary>

```python
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

   
```
</details>
    
#### Text Analysis:

In this section, I aim to understand the power of video titles in YouTube content. I use the 'title' column to extract the text of video titles and then apply a sentiment analysis tool to classify them as positive, negative, or neutral. Then, I will proivde answers to the following questions:

*1. Perform sentiment analysis on video titles. Are positive, neutral, or negative titles more engaging?* 

This allows me to 'Perform sentiment analysis on video titles' and see how the tone of titles affects the engagement of videos.

<!-- Embed the Plotly plot using an iframe -->
<iframe src="sentiment-engagement.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the average engagement score by sentiment. It reveals that the neutral sentiment has the highest average engagement score, followed by the positive sentiment, and the negative sentiment has the lowest average engagement score. This could suggest that the viewers are more interested or curious about the videos that have a neutral tone or perspective, rather than those that have a positive or negative tone or perspective. This could also imply that the viewers are more likely to engage with videos that are balanced, objective, or informative, rather than those that are biased, subjective, or emotional. The graph also shows the importance of understanding the audience's preferences and expectations when creating video content.


*2. Analyze the most common words or phrases in video titles?* 

I also analyze the 'Most common words or phrases in video titles' by using a word frequency tool to count the occurrence of words or phrases in the titles. This helps me identify the most popular topics or keywords in video titles and how they relate to viewer interests. This analysis takes me through the secrets of video titles, revealing how they influence viewer behavior and preferences.

<!-- Embed the Plotly plot using an iframe -->
<iframe src="sentiment-wordcloud.html" width="800" height="600" frameborder="0"></iframe>

The word cloud image shows the terms related to artificial intelligence. It suggests that artificial intelligence is a central and prominent topic that has many associations and implications. The words around it are in different colors and sizes, indicating the diversity and complexity of the artificial intelligence field. The words also reflect the different aspects, perspectives, or opinions on artificial intelligence, such as its tools, applications, benefits, risks, or challenges. For example, "robot" might be related to the technology or innovation of artificial intelligence. "Future" might be related to the vision or expectation of artificial intelligence. "Elon Musk" might be related to the influence or controversy of artificial intelligence. The word cloud also shows the interest or curiosity of the viewers or the creators about artificial intelligence.

<iframe src="sentiment-word-bar.html" width="800" height="600" frameborder="0"></iframe>

The bar graph shows the frequency of the most common words/phrases in video titles. It indicates that the video titles tend to use words/phrases that are related to animals, humor, emotions, nature, science, or the world. This could reflect the popularity or appeal of these topics among the viewers or the creators. For example, "animal" might be the most common word/phrase because it attracts attention, curiosity, or empathy from the viewers. "Humanity" might be the least common word/phrase because it is too vague, abstract, or controversial for the viewers. The graph also shows the potential for creating video titles that are catchy, relevant, or unique.

<details>
<summary style="color: green;">Click to reveal code</summary>

```python
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

   
```
</details>