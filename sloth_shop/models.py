from django.db import models
from django.urls import reverse 

# Category Model with use of slug
# 'def get_url" used to give categories a link

class Category(models.Model):
  name = models.CharField(max_length=250, unique=True)
  slug = models.CharField(max_length=250, unique=True)
  description = models.TextField(blank=True)
  image = models.ImageField(upload_to='sloth_category', blank=True)

  class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def get_url(self):
    return reverse('shop:products_by_category', args=[self.slug])
  
  def __str__(self):
    return '{}'.format(self.name)


    