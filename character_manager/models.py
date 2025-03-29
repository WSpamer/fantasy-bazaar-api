from django.db import models
from campaign_manager.models import Campaign


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Occupation(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Race(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class NPC(models.Model):

    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    occupation = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    relationship_level = models.IntegerField()
    notes = models.TextField()
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.name


# TODO: Add a foreign key to the User model
class Character(models.Model):

    name = models.CharField(max_length=100, unique=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    # TODO: Add a foreign key to the User model

    def __str__(self):
        return self.name
