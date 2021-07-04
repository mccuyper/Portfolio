from django.contrib import admin
from .models import MyPersonalData, Blog, ContactForm, Portfolio


admin.site.register(MyPersonalData)
admin.site.register(Blog)
admin.site.register(ContactForm)
admin.site.register(Portfolio)