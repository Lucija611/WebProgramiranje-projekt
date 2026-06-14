from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.home, name='home'),
    path('literature/', views.literature, name='literature'),
    path('upload/', views.upload_note, name='upload_note'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
]