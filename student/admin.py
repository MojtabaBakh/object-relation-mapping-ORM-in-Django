from django.contrib import admin
from .models import Student , Course , Lesson , Package

# Register your models here.

admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Course)
admin.site.register(Package)

