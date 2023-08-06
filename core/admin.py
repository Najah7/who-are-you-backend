from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.SNS)
admin.site.register(models.Others)

# Register your models here.
