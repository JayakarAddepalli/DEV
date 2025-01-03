from django.contrib import admin
from .models import *

# Register your models here.

class homeModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo')

class hashTagsModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

class pythonBlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topics', 'description')

class topics_ModelAdmin(admin.ModelAdmin):
    list_display = ('content',)

class htmlBlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topics', 'description')

class htmltopics_ModelAdmin(admin.ModelAdmin):
    list_display = ('content',)

class cssBlogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'topics', 'description')

class csstopics_ModelAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(homeModel, homeModelAdmin)
admin.site.register(hashTagsModel, hashTagsModelAdmin)
admin.site.register(PythonBlogsModel, pythonBlogsAdmin)
admin.site.register(TopicModel, topics_ModelAdmin)
admin.site.register(HTMLBlogsModel, htmlBlogsAdmin)
admin.site.register(HTMLTopicModel, htmltopics_ModelAdmin)
admin.site.register(CSSBlogsModel, cssBlogsAdmin)
admin.site.register(CSSTopicModel, csstopics_ModelAdmin)