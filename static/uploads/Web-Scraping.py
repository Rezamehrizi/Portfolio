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