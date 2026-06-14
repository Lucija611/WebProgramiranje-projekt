from django.contrib import admin
from .models import Note, Review, Profile

admin.site.register(Note)
admin.site.register(Review)
admin.site.register(Profile)