from django.urls import path
from .views import voice_home, history_view, delete_voice, save_speech
from voice import views

urlpatterns = [
    path('', voice_home, name='voice_home'),
    path('history/', history_view, name='history'),
    path('delete/<int:id>/', delete_voice, name='delete_voice'),
    path('save-speech/', save_speech, name='save_speech'),
    path('suggest-text/', views.suggest_text, name='suggest_text'),
]