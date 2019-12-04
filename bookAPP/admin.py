from django.contrib import admin

# Register your models here.
from bookAPP import models
admin.site.register(models.authorinfo)
admin.site.register(models.authordetails)
admin.site.register(models.bookinfo)
admin.site.register(models.publishinfo)
