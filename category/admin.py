from django.contrib import admin
from .models import questionCategory

# Register your models here.
class categoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('categoryName',)}

admin.site.register(questionCategory, categoryAdmin)