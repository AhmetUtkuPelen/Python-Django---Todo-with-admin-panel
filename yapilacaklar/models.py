from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = 'name', unique=True)

    def __str__(self):
        return self.name
    

class SubCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from = 'name', unique=True)

    def __str__(self):
        return self.name
    


class ToDo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.FileField(upload_to='todo_picture', null=True, blank=True)

    slug = AutoSlugField(populate_from = "title", unique=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    sub_category = models.ManyToManyField(SubCategory)

    def __str__(self):
        return self.title