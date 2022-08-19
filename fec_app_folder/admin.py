from django.contrib import admin
from .models import UserDB, SolidDB, TemporaryDB, AssetDB


admin.site.register(UserDB)
admin.site.register(SolidDB)
admin.site.register(TemporaryDB)
admin.site.register(AssetDB)