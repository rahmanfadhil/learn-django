from django.shortcuts import render


posts = [
    {
        'title': 'Blog Post 1',
        'content': 'First blog post content',
        'author': 'Rahman Fadhil',
        'date_posted': 'August 27, 2019'
    },
    {
        'title': 'Blog Post 2',
        'content': 'Second blog post content',
        'author': 'Rahman Fadhil',
        'date_posted': 'August 28, 2019'
    },
]


def home(request):
    context = {'posts': posts}
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html')
