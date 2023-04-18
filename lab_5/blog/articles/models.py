from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __unicode__ (self):
       # return "%s: %s" % (self.author.username, self.title)
        return "%s: %s: %s " % (self.author.username, self.title, self.text)
    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text
