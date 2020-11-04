from django.shortcuts import render

posts = [
    {
        'author': 'Kieran Smith',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'datePosted': 'November 4th 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'datePosted': 'November 5th 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

# Create your views here.
