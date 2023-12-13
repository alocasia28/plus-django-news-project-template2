from django.urls import path
from . import views


app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(),name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/comment', views.CommentView.as_view(), name='commentForm'),
    path('<int:pk>/edit', views.UpdateStoryView.as_view(), name='updateStory'),
    path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory'),
    # path('author/<str:username>', views.AuthorSearchView.as_view(), name='author_search'),
    # path('author/<str:username>', views.AuthorDetailView.as_view(), name='authordetail'),
]
