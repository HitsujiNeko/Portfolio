from django.contrib import admin
from .models import MySkill, MyQualification

# Register your models here.
admin.site.register(MySkill)
admin.site.register(MyQualification)