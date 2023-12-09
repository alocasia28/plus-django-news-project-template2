from django.db import models


class NewsStory(models.Model): #tells django what a news story looks like and create new stores or get existing ones from db
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
