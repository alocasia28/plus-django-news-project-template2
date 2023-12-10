from django.db import models
from django.contrib.auth import get_user_model

class NewsStory(models.Model): #tells django what a news story looks like and create new stores or get existing ones from db
    Category_Choices = [
    ('Technology', 'Technology'),
    ('Rest of World', ' Rest of World'),
    ('Australia', 'Australia'),
    ('Business', 'Business'),
    ('Sports', 'Sports')

    ]
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="stories"
    )
    category = models.CharField(max_length=20, blank=False, choices=Category_Choices, default= "No Category")
    tag_line = models.CharField(max_length=500)
    pub_date = models.DateTimeField()
    content = models.TextField()
    story_image_URL = models.URLField(default="No URL Defined")

class Comment(models.Model):
    news_story = models.ForeignKey(
        NewsStory,
        on_delete=models.CASCADE,
        related_name='comments')
    message = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    name = models.ForeignKey(
        get_user_model(),
        related_name="comments",
        on_delete=models.CASCADE
    )