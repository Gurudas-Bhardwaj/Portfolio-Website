from django.contrib import admin
from .models import Contact

class Details(admin.ModelAdmin):
    list_display=("Name","Email","Subject")

admin.site.register(Contact,Details)