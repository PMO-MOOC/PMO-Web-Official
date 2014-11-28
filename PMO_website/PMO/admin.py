from django.contrib import admin

# Register your models here.
from PMO.models import User

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		('User',               {'fields': ['user_name']}),
		('Announcement date', {'fields': ['pub_date']}),
		('Announcement', {'fields':['recent_upload'],'classes': ['collapse']})
		]
	list_display = ('user_name', 'pub_date')
admin.site.register(User, UserAdmin)