from django.contrib import admin
from  .models import employee

# Register your models here.
@admin.register(employee)
class newadmin(admin.ModelAdmin):
    list_display=["name","company"]

