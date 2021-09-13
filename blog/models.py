from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to = 'media/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]