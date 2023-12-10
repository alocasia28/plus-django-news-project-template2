from django.contrib import admin
from .models import NewsStory

# Register your models here.
@admin.register(NewsStory)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','author','category','tag_line','pub_date','content','story_image_URL')
    # date_hierarchy = 'created' 
    # search_fields = ('author')