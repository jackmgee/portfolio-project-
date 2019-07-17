from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length= 30 )
    image = models.ImageField(upload_to='images/')
    Body = models.TextField()
    Date = models.DateTimeField()
