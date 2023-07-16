from django.views.generic import ListView, DetailView
from .models import Post
from datetime import datetime

class PostList(ListView):
    model = Post
    ordering = 'post_header'
    template_name = 'news.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class Event(DetailView):
    model = Post
    template_name = 'event.html'
    context_object_name = 'event'
