from django.shortcuts import render
from .models import Post

# posts = [
#     {
#         'author': 'Ram Pd',
#         'title' : 'Blog post 1',
#         'content': 'First Post Content',
#         'date_posted': 'August 28 2019'
#     },
#     {
#         'author': 'Sita Maya',
#         'title' : 'Blog post 2',
#         'content': 'Second Post Content',
#         'date_posted': 'August 27 2019'
#     },
# ]

# Create your views here.
def home(request):
    context = {
        'posts_context': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title_presented':'about'})
