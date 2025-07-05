from googleapiclient.discovery import build
from .config import YOUTUBE_API_KEY


def search_youtube(query):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

    request = youtube.search().list(
        part='snippet',
        q=query,
        type='video',
        maxResults=3  # Show 3 videos per character
    )

    response = request.execute()

    videos = []
    for item in response['items']:
        video_id = item['id']['videoId']
        title = item['snippet']['title']
        videos.append({
            'title': title,
            'url': f'https://www.youtube.com/watch?v={video_id}'
        })

    return videos
