from django.shortcuts import render
from django.utils import timezone
from segundaApp.models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'segundaApp/post_list.html', {'posts' : posts})