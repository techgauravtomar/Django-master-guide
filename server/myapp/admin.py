from django.contrib import admin
from .models import StudentModel,Movie

# Register your models here.

admin.site.register(StudentModel)

#upload
admin.site.register(Movie)


