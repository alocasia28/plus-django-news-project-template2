# from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, FormView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'



class MyProfileView(TemplateView):
    model = CustomUser
    success_url = reverse_lazy('myProfile')
    template_name = 'users/my-profile.html'

    def get_object(self, *args, **kwargs):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_stories'] = NewsStory.objects.filter(author=self.request.user)
        return context
    #slight issue with this one. If a user is not logged in and you try to access /users/my-profile/ you get a TypeError since it needed an id to match it to the user
    
# class SearchView(FormView):
#     model = CustomUser
#     template_name = 'search.html'
#     form_class = SearchForm

#     def get_queryset(self): 
#         query = self.request.GET.get('q')
#         object_list = NewsStory.objects.filter(
#             Q(username__icontains='admin')
#         )
#         return object_list


# class SearchView(generic.Detailview):
#     model = CustomUser
#     template_name = 'news/index.html'
#     context_object_name = 'author'

#     def get_object(self, *args, **kwargs):
#         return get_object_or_404(CustomUser,username=self.kwargs['username'])
#     # Need to change this to get input from a search bar

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['author_stories'] = NewsStory.objects.filter(author=self.request.user)
#         return context