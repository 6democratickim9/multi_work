from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id','productname','count_text'] #--> id, title, count_text를 상단에 보여주겠다
    list_display_links = ['productname'] #-->title 에 링크를 걸어서 게시글로 들어갈 수 있게 해주겠다


    def count_text(self, obj):
        return '{}글자'.format(len(obj.text))
    count_text.short_description = '내용 글자수' #--> count text 부분 대신에 내용 글자수로 대체됨

admin.site.register(Post,PostAdmin)