from django.shortcuts import render
from blog.data import posts
from typing import Any
from django.http import HttpRequest, Http404
# Create your views here.

def blog1(request):
    context = {
            #'text' : 'blog vazio',
            'title' : 'Blog do Mathias -',
            'posts' : posts,
            'id' : posts,
}
    return render(
        request, 
        'blog.html',
        context,

    )

def post(request:HttpRequest, post_id:int):
    found_post: dict[str, Any] | None = None
    
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    if found_post is None:
        raise Http404('''Post doesn't exist.''')

    context = {
            #'text' : 'blog vazio',
            'title' : found_post['title'] + ' -',
            'post' : found_post,
            'id' : posts,
}
    return render(
        request, 
        'post.html',
        context,

    )


def teste(request):
    context = {
            'text' : 'Test empty.',
            'title' : 'Test (Blog) -'
}
    return render(
        request,
        'teste_blog.html',
        context,
    )