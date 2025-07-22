from django.shortcuts import render
import wikipediaapi
from .models import Character
from .utils import search_youtube
from .config import STRAWHAT_CREW
from urllib.parse import urlparse, parse_qs  # 👈 Add this import


wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='onepiece-fanverse-app/1.0 (prathamesh@example.com)'
)

# 👇 Helper function to extract video ID from YouTube URL
def extract_video_id(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
            return parse_qs(parsed_url.query).get('v', [None])[0]
    except:
        return None

def home(request):
    return render(request, 'home.html')

def show_characters(request):
    strawhats = STRAWHAT_CREW
    return render(request, 'characters.html', {'characters': strawhats})

def character_detail(request, name):
    page = wiki.page(name)
    description = page.summary
    Character.objects.get_or_create(name=name, defaults={'description': description})
    return render(request, 'detail.html', {'name': name, 'summary': description})

def show_action(request):
    strawhats = STRAWHAT_CREW
    return render(request, 'action.html', {'characters': strawhats})

def action_detail(request, name):
    query = f"{name} one piece fight scene"
    videos = search_youtube(query)

    # 👇 Add video_id to each video dict
    for video in videos:
        video['video_id'] = extract_video_id(video['url'])

    return render(request, 'action_detail.html', {'name': name, 'videos': videos})