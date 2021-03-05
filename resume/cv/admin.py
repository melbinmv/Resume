from django.contrib import admin
from .models import about,Project,Skills,Say,Resume
# Register your models here.
admin.site.register(about)
admin.site.register(Project)
admin.site.register(Skills)
admin.site.register(Say)
admin.site.register(Resume)