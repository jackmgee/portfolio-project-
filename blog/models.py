from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length= 30 )
    image = models.ImageField(upload_to='images/')
    Body = models.TextField()
    Date = models.DateTimeField()

    def summary(self):
        return self.Body[:100]

    def __str__(self):
        return self.title



