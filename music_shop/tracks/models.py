from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def str(self):
        return self.name

class Track(models.Model):
    title = models.CharField(max_length=200)
    release_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='tracks')

    def str(self):
        return self.title
