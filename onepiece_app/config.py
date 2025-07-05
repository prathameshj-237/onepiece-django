import os
from dotenv import load_dotenv

load_dotenv()

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

STRAWHAT_CREW = [
    "Luffy", "Zoro", "Nami", "Sanji", "Usopp",
    "Robin", "Chopper", "Franky", "Brook", "Jinbe"
]
