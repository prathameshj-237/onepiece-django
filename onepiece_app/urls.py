from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.show_characters, name='show_characters'),
    path('characters/<str:name>/', views.character_detail, name='character_detail'),  # <--- This line is crucial
    path('action/', views.show_action, name='show_action'),
    path('action/<str:name>/', views.action_detail, name='action_detail'),
]
