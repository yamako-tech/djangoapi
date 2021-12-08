from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id) + " - " + self.title
    
    class Meta:
        ordering = ["-created"]

class Todo(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id) + " - " + self.title
    
    class Meta:
        ordering = ["-created"]
