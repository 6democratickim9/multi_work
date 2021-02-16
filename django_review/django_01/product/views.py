from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from requests import post
from pathlib import Path
from django.contrib.auth.models import User

from .models import Post

# Post 삭제


# post 상세정보

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request,'product/post_detail.html',{'post': post})



# Post 목록

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'product/post_list.html', {'posts': posts})


    #
    # # Post 목록
    # def post_response(request):
    #     name = 'Django'
    #     response = HttpResponse(f'<h2>Hello {name}</h2>',content_type ="text/html")
    #     response.write(f'<h2>Hello {name}</h2>')
    #     response.write(f'<p>HTTP Method : {request.method}</p>')
    #     response.write(f'<p>HTTP ConentType : {request.content_type}</p>')
    #     # return HttpResponse(f'''<h2>Hello{name}</h2><p>HTTP METHOD : {request.method}</p>''')
    #
    #     return response