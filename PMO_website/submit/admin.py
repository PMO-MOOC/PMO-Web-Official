from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from submit.models import Partners, Groups 


class MemberInline(admin.TabularInline):
    model = Partners
    extra = 3


class GroupAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['group_name']}),
		('Date information', {'fields': ['sub_date'],'classes': ['collapse']}),
		('Select file' ,     {'fields': ['docfile']}),
		('Summary' ,     {'fields': ['summary']}),
		('Source url' ,     {'fields': ['src_url']}),
		('Document url' ,     {'fields': ['doc_url']}),  
	]
	inlines = [MemberInline]
	
	list_display = ('group_name', 'sub_date', 'file_location')
	list_filter = ['published']
admin.site.register(Groups, GroupAdmin)


# Register your models here.
