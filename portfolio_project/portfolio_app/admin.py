from django.contrib import admin
from .models import Profile,MySkill, MyQualification, App,BlogPost

# Register your models here.
admin.site.register(Profile)
admin.site.register(MySkill)
admin.site.register(MyQualification)
admin.site.register(App)
admin.site.register(BlogPost)
