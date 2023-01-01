from django.contrib import admin

# Register your models here.

from .models import Test


class TestAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )

admin.site.register(Test, TestAdmin)
