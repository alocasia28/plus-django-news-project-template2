from typing import Any
from urllib.request import Request
from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Comment
from .forms import StoryForm, CommentForm
from users.models import CustomUser
from django.db.models import Q #new

#this is the code I'm hoping will do partial matches on the input and return against username or cateogry
# class IndexView(generic.ListView):
#     template_name = 'news/index.html'
#     context_object_name = "all_stories"


    # def get_queryset(self):
    #     '''Return all news stories.'''
    #     search = self.request.GET.get('search', None)
    #     if (search != None):
    #         return NewsStory.objects.filter(author__username__icontains=search).order_by('-pub_date').__or__(category__icontains=search).order_by('-pub_date')
    #     else:
    #         return NewsStory.objects.all().order_by('-pub_date')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     search = self.request.GET.get('search', None)
    #     if (search == None):
    #         context['latest_stories'] = (NewsStory.objects.all().order_by("-pub_date") [:4])
    #     else:
    #         context ['filtering'] = True
    #         context['latest_stories'] = NewsStory.objects.filter(author__username__icontains=search).order_by('-pub_date').__or__(category__icontains=search).order_by('-pub_date')
    #     return context
# This is the working index view with searching based on author
class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        author_name = self.request.GET.get('author', None)
        if (author_name != None):
            return NewsStory.objects.filter(author__username__icontains=author_name).order_by('-pub_date')
        else:
            return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author_name = self.request.GET.get('author', None)
        if (author_name == None):
            context['latest_stories'] = (NewsStory.objects.all().order_by("-pub_date") [:4])
        else:
            context ['filtering'] = True
            context['latest_stories'] = NewsStory.objects.filter(author__username__icontains=author_name).order_by('-pub_date')
        return context
    
    
class StoryView(generic.DetailView):
    model = NewsStory #type of record for django to look at 
    template_name = 'news/story.html' #template django should use
    context_object_name = 'story' #this is me naming it. 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdateStoryView(generic.UpdateView):
    model=NewsStory
    template_name = "news/updateStory.html"
    fields = ['title','category', 'story_image_URL', 'pub_date', 'content']
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# def DeleteSuccessView(request):
#     return render(request,'news.deleteSuccess,html')

# class DeleteStoryView(generic.DeleteView):
#     model = NewsStory
#     template_name = 'news/deleteStory.html'
#     success_url = reverse_lazy('news:index')
#     context_object_name = 'deletestory'

#     def get_context_data(self, **kwargs: Any):
#         context = super().get_context_data(**kwargs)
#         context['story'] = NewsStory.objects.get(id=self.kwargs['pk'])
#         return context
class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = "news/deleteStory.html"
    fields = ['title','category', 'story_image_URL', 'pub_date', 'content']
    success_url = reverse_lazy('news:index')
    
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class CommentView(generic.CreateView):
    form_class = CommentForm
    context_object_name = 'commentform'
    template_name = 'news/story.html'

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk")) 
    
    def form_valid(self, form):     
        form.instance.name = self.request.user
        pk = self.kwargs.get("pk")
        related_story = get_object_or_404(NewsStory, pk=pk)
        form.instance.news_story = related_story
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get("pk")})

# class AuthorSearchView(generic.ListView):
#     template_name = 'news/search_results'
#     context_object_name = "author_search"

#     def get_queryset(self):
#         '''Return all news stories.'''
#         author_name = self.request.GET.get('author', None)
#         if (author_name != None):
#             return NewsStory.objects.filter(author__username=author_name).order_by('-pub_date')
#         else:
#             return NewsStory.objects.all().order_by('-pub_date')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         author_name = self.request.GET.get('author', None)
#         if (author_name == None):
#             context['latest_stories'] = (NewsStory.objects.all().order_by("-pub_date") [:4])
#         else:
#             # context ['filtering'] = True
#             context['latest_stories'] = NewsStory.objects.filter(author__username=author_name).order_by('-pub_date')
#         return context
    
#     def get_success_url(self):
#         return reverse_lazy('news:author_search', kwargs={'author':self.kwargs.get("author")})