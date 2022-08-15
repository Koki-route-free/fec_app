from django.contrib import admin
from .models import UserDB, SolidDB, TemporaryDB, AssetDB
# Register your models here.

admin.site.register(UserDB)
admin.site.register(SolidDB)
admin.site.register(TemporaryDB)
admin.site.register(AssetDB)