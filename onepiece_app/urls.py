from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('characters/', views.show_characters, name='characters'),
    path('characters/<str:name>/', views.character_detail, name='detail'),
    path('action/', views.show_action, name='action'),
    path('action/<str:name>/', views.action_detail, name='action_detail'),
]
