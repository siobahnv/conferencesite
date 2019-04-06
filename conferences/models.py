from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_title = models.CharField(max_length=100)
    article_content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')
