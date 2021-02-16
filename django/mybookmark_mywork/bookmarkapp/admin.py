from bookmarkapp.models import Bookmark
from django.contrib import admin

# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title','url')


admin.site.register(Bookmark,BookmarkAdmin)
