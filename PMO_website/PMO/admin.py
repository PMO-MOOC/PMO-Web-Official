from django.contrib import admin

# Register your models here.
from PMO.models import User
from PMO.models import Question
from PMO.models import Post

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		('User',               {'fields': ['user_name']}),
		('Announcement date', {'fields': ['pub_date']}),
		('Announcement', {'fields':['recent_upload'],'classes': ['collapse']})
		]
	list_display = ('user_name', 'pub_date')
        
admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Post)
