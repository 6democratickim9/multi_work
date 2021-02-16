from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):

    title = models.CharField('TITLE',max_length=50)
    slug = models.SlugField('SLUG',unique=True,allow_unicode=True,help_text='one word for this alias')
    description = models.CharField('DESCRIPTION',max_length=100,blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_date = models.DateTimeField('Create Date',auto_now_add = True)
    modify_date = models.DateTimeField('Modify Date',auto_now = True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'blog_posts'
        ordering = ('-modify_date',)        #얘는 내림차순
        # 오림차순: ascending
        #내림차순: descending,

    def get_absolute_url(self):
        return reverse('blog:post_detail',args=(self.slug,))#주소체계로 이동--> 슬러그로 이동한 데이터값이 디테일로 올라갈거임
    def get_previous_post(self):
        return self.get_previous_by_modify_date()

    def get_next_post(self):
        return self.get_next_by_modify_date()
    