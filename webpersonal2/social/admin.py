from django.contrib import admin
from .models import Social
# Register your models here.
class SocialAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

    def get_readonly_fields(self,request, obj=None):
        if request.user.groupes.filter(name="Personal").exists():
            return('created','updated','key','name')
        else:
            return('created','updated')
admin.site.register(Social, SocialAdmin)