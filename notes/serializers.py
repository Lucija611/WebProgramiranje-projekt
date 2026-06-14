from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['id', 'title', 'course_name', 'faculty', 'author', 'average_rating']

    def get_average_rating(self, obj):
        return obj.average_rating()