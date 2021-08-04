from django.contrib import admin

from.models import BgModel

class BgAdmin(admin.ModelAdmin):
	list_display = ("title", "post_updated")
	list_filter = ("post_updated",)
admin.site.register(BgModel, BgAdmin)
