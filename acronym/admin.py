from django.contrib import admin
from .models import Acronym, Users, Suggestions

# Register your models here.
class AcronymAdmin(admin.ModelAdmin):
    pass

class SuggestionsAdmin(admin.ModelAdmin):
    pass

class UsersAdmin(admin.ModelAdmin):
    pass

admin.site.register(Acronym)
admin.site.register(Users)
admin.site.register(Suggestions)