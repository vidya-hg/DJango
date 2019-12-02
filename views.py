from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'VidyaHG',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'November 27, 2019'
    },
    {
        'author': 'ShailendraY',
        'title': 'Blog Post 3',
        'content': 'Second post content',
        'date_posted': 'November 28, 2019'
    },
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About'})
