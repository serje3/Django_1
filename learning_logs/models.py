from django.db import models
from django.contrib.auth.models import User



class Topic(models.Model):
    text = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    count_entries = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.text
class Entry(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.TextField(default='')
    text = models.TextField()
    tags = models.ManyToManyField('Tag',blank=True)
    #likes = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural='entries'

    def __str__(self):
        return self.text[:50]+"..."

class Tag(models.Model):
    title = models.CharField(max_length=50)


    def __str__(self):
        return self.title