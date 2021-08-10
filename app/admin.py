from django.contrib import admin
from .models import MyPersonalData, Blog, ContactForm, Portfolio


admin.site.register(MyPersonalData)

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("css/main.css",)}
        js = ("js/blog.js",)

admin.site.register(Blog, BlogAdmin)
admin.site.register(ContactForm)
admin.site.register(Portfolio)
