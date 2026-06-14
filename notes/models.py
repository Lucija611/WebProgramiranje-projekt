from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username} - {self.faculty}"


class Note(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    faculty = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='notes/files/')
    created_at = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name='favorite_notes', blank=True)

    def __str__(self):
        return f"{self.title} ({self.course_name}) by {self.author.username}"

    def is_favorited_by(self, user):
        if not user.is_authenticated:
            return False
        return self.favorited_by.filter(id=user.id).exists()

    def favorite_count(self):
        return self.favorited_by.count()

    def average_rating(self):
        avg = self.review_set.aggregate(Avg('rating'))['rating__avg']
        if avg is None:
            return None
        return round(avg, 1)


class Review(models.Model):
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    rating = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.note.title} by {self.reviewer.username}"