from django.contrib import admin
from .models import Ask,Comment,Questions,Answers

# Register your models here.
admin.site.register(Ask)
admin.site.register(Comment)
admin.site.register(Questions)
admin.site.register(Answers)