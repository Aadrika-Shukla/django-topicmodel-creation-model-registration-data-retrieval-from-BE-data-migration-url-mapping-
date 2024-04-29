from django.contrib import admin

# Register your models(tables for the database) here.
# for registering the models to admin register word r should always be in lowercase else it will not get register
from app.models import *

admin.site.register(Topic)

admin.site.register(WebPage)

admin.site.register(AccessRecord)
