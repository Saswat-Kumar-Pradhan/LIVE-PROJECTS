from django.urls import path
from .views import send_youtube_monthly_split

urlpatterns = [
    path('send-month-email/', send_youtube_monthly_split, name='send_youtube_monthly_split'),
]
