from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Cloth

# Register your models here.
# User 모델을 등록해줘야함
admin.site.register(User, UserAdmin)
admin.site.register(Cloth) #Cloth 모델 등록, admin 사이트에 반영
UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)