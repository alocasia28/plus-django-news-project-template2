from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory, Comment
from .forms import StoryForm, CommentForm
from users.models import CustomUser


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = (NewsStory.objects.all().order_by("-pub_date") [:4])
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

