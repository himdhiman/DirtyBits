from django.db import models

# Create your models here.

class Problem(models.Model):
    difficulty_level = [
        ('e', 'easy'),
        ('m', 'medium'),
        ('h', 'hard')
    ]
    part = [
        ('ll', 'Linked List'),
        ('q', 'Queue')
    ]
    name = models.CharField(max_length = 50)
    description = models.TextField()
    image = models.ImageField()
    level = models.CharField(max_length = 10, choices = difficulty_level)
    topic = models.CharField(max_length = 100, choices = part)

    def __str__(self):
        return self.name