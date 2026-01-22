from django.contrib import admin
from .models import AboutUs, post,category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display=("title","content")
    search_fields=("title","content")
    list_filter=("category","created_at")

admin.site.register(post,PostAdmin)
admin.site.register(category)
admin.site.register(AboutUs)

