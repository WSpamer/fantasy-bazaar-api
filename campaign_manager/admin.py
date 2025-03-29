from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Faction)
admin.site.register(models.OrganizationType)
admin.site.register(models.Country)
admin.site.register(models.Religion)
