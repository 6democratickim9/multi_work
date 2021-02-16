from django.urls import path, include
from api.views import PostViewSet

app_name = 'api'

post_list = PostViewSet.as_view({ 'get':'list'})
 = PostViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('',include('rest_framework.urls',namespace='rest_framework')),
    path('posts/',post_list, name='post_list'),
    path('posts/<int:pk>',post_detail, name='post_detail'),
    
]
