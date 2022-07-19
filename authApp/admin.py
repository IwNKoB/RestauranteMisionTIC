from django.contrib import admin
from .models.user import User
from .models.account import Account
from authApp.models import user

admin.site.register(User)
admin.site.register(Account)


# Register your models here.
