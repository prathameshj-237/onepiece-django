from django.shortcuts import render
import wikipediaapi
from .models import Character
from .utils import search_youtube
from .config import STRAWHAT_CREW


wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='onepiece-fanverse-app/1.0 (prathamesh@example.com)'
)

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
    return render(request, 'action_detail.html', {'name': name, 'videos': videos})

