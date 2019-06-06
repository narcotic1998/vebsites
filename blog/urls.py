from django.conf.urls import url, include
from blog.models import Post
from blog.views import BlogView, PostView
urlpatterns =[

                    url(r'^$',BlogView.as_view()),

                url(r'^(?P<pk>\d+)$',PostView.as_view())
                ]
