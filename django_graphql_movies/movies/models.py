from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    year = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
