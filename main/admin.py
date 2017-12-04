from django.contrib import admin
from .models import Contacts, Groups,GroupsToUser


admin.site.register(Contacts)
admin.site.register(Groups)
admin.site.register(GroupsToUser)