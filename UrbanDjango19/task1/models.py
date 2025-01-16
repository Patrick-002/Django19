from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField()

class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


# from task1.models import Buyer, Game
# Game.objects.all()
# Buyer.objects.create(name = 'user1', balance = 777.77, age = 22)
# Game.objects.create(title = 'RainWorld', cost = 880, size = 8, description = 'Slugcat <3', age_limited = 0)
# Game.objects.get(id=1).buyer.set((Nikita, user1))
