from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    # /blog/
    path('', PostLV.as_view(), name='index'),

    # /blog/post
    path('post/', PostLV.as_view(), name='post_list'),

    # /blog/post/{SLUG}
    path('post/<str:slug>', PostDV.as_view(), name='post_detail'),

    # Example: /archive/
    path('archive/', PostAV.as_view(), name='post_archive'),

    # Example: /2021/
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),

    # Example: /2021/01/
    path('<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),

    # Example: /2021/01/21/
    path('<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),

    # Example: /today/ -> http://127.0.0.1:8000/blog/today/
    path('today/', PostTAV.as_view(), name='post_today_archive'),

    path('search/',SearchFormView.as_view(), name='search'),

]
