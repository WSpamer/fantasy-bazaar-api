from django.db import models
from character_manager.models import NPC


# Create your models here.
# TODO: Add a field to NPC to link it to a campaign
# TODO: Add a field to identify if a campaign is active or inactive
# TODO: Add a field to identify if a campaign is homebrew or not
class Campaign(models.Model):

    name = models.CharField(max_length=100, unique=True)
    source = models.CharField(max_length=100)  # e.g. D&D, Pathfinder
    is_homebrew = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Faction(models.Model):

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100)
    description = models.TextField()
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.name


class OrganizationType(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Organization(models.Model):

    name = models.CharField(max_length=100, unique=True)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    description = models.TextField()
    type = models.ForeignKey(OrganizationType, on_delete=models.CASCADE)
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.name


class Religion(models.Model):

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Country(models.Model):

    name = models.CharField(max_length=100, unique=True)
    relationship = models.TextField()
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    unique_laws = models.TextField()
    notes = models.TextField()
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.name


class PointOfInterest(models.Model):

    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.name


class Town(models.Model):

    name = models.CharField(max_length=100, unique=True)
    pointOfInterest = models.ForeignKey(PointOfInterest, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Building(models.Model):

    name = models.CharField(max_length=100, unique=True)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
