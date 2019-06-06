from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post

class BlogView(ListView):
        model =Post
        template_name="blog/blog.html"
        def get_context_data(self,**kwargs):
            context = super(BlogView,self).get_context_data(**kwargs)
            context['post_list'] = Post.objects.all().order_by("date")[:25]
            context["blog"] = "active"
            context["title"] = "Blog"
            return context
class PostView(DetailView):
    model = Post
    template_name="blog/post.html"
    def get_context_data(self,**kwargs):
        context = super(PostView,self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all().order_by("date")[:25]
        context["blog"] = "active"
        context["title"] = "Blog"
        return context
