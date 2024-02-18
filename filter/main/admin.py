from django.contrib import admin
from .models import gurukul
# Register your models here.
@admin.register(gurukul)
class new(admin.ModelAdmin):
    list_display=["name","guruname"]