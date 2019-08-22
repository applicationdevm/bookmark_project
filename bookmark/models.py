from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=30,verbose_name = '사이트명')
    url = models.URLField(verbose_name='주소')
    description  = models.TextField(blank=True,verbose_name = '설명')

    def __str__(self):
        return self.site_name+' : '+self.url

    class Meta:
        ordering = ['site_name']
