from django.contrib import admin

# Register your models(tables for the database) here.
from app.models import *

admin.site.register(Topic)

admin.site.register(WebPage)

admin.site.register(AccessRecord)
