from django.db import models
from django.contrib.auth.models import User

from templates.product.models import MainContent

class Comment(models.Model):
 author = models.ForeignKey(User, on_delete=models.CASCADE)
 content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
 content = models.TextField()
 create_date = models.DateTimeField(auto_now_add=True)
 modify_date = models.DateTimeField(auto_now=True)

 def __str__(self):
  return self.title