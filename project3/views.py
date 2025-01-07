from datetime import datetime
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from .models import *

def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'list_post.html', {'posts': posts})

#def post_detail(request, pk):
 #   post = get_object_or_404(Post, pk=pk)
  #  post.counted_views = post.counted_views + 1
   # post.save()
    #return render(request, 'post_detail.html', {'post': post})


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        post.counted_views += 1
        post.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object

        previous_post = Post.objects.filter(published_date__lt=post.published_date).order_by('-published_date').first()
        next_post = Post.objects.filter(published_date__gt=post.published_date).order_by('published_date').first()

        context['previous_post'] = previous_post
        context['next_post'] = next_post
        return context

# Create your views here.
