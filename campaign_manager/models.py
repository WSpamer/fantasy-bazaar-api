from django.db import models


# Create your models here.
class Faction(models.Model):

    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=100)
    description = models.TextField()
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
    unique_laws = models.TextField()
    notes = models.TextField()
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.name


class Location(models.Model):

    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class PointsOfInterest(models.Model):

    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateField()
    updated = models.DateField()

    def __str__(self):
        return self.name


class Town(models.Model):

    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
