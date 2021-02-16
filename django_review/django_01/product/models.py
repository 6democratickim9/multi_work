from django.db import models
from django.utils import timezone


class Post(models.Model):

    name = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    productname = models.CharField(max_length=300)
    price = models.BigIntegerField()
    stock_quantity = models.BigIntegerField()
    description = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)



    def __str__(self):
        return self.productname

    def publish(self):
        self.published_date = timezone.now()
        self.save()