from django.db import models

# Create your models here.
class homeModel(models.Model):
    logo = models.ImageField(upload_to='homeImages/')

class hashTagsModel(models.Model):
    title = models.CharField(max_length=50)

class PythonBlogsModel(models.Model):
    topics = models.CharField(max_length=50)
    description = models.TextField()
    
class TopicModel(models.Model):
    content = models.TextField()

class HTMLBlogsModel(models.Model):
    topics = models.CharField(max_length=50)
    description = models.TextField()

class HTMLTopicModel(models.Model):
    content = models.TextField()

class CSSBlogsModel(models.Model):
    topics = models.CharField(max_length=50)
    description = models.TextField()
    
class CSSTopicModel(models.Model):
    content = models.TextField()