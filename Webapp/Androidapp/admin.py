from django.contrib import admin
from Androidapp.models import AndroidApp
from Androidapp.models import UserTask
from Androidapp.models import UserProfile
from Androidapp.models import Admin
admin.site.register(AndroidApp)
admin.site.register(UserProfile)
admin.site.register(UserTask)
admin.site.register(Admin)
# Register your models here.
