from django.urls import path
from . import views

app_name = "gpt"
urlpatterns = [
    path('', views.generate_text, name='gpt'),
]
