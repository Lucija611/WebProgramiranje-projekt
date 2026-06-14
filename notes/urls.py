from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [
    path('', views.home, name='home'),
    path('literature/', views.literature, name='literature'),
    path('upload/', views.upload_note, name='upload_note'),
    path('note/<int:note_id>/', views.note_detail, name='note_detail'),
    path('note/<int:note_id>/download/', views.download_note, name='download_note'),
    path('note/<int:note_id>/edit/', views.edit_note, name='edit_note'),
    path('note/<int:note_id>/delete/', views.delete_note, name='delete_note'),
    path('note/<int:note_id>/review/', views.add_review, name='add_review'),
    path('note/<int:note_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),

    # API rute
    path('api/notes/', views.api_notes, name='api_notes'),
    path('api/notes/<int:note_id>/favorite/', views.api_toggle_favorite, name='api_toggle_favorite'),
]