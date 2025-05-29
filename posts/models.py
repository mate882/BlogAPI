from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='posts/', default='static/images/default.jpg', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  