from django.urls import path
from .views import send_youtube_monthly_split, send_youtube_monthly_receipt

urlpatterns = [
    path('send-month-email/', send_youtube_monthly_split, name='send_youtube_monthly_split'),
    path('send-month-receipt/', send_youtube_monthly_receipt, name='send_youtube_monthly_receipt'),
]
