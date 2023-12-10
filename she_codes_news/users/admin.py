from django.contrib import admin
from .models import CustomUser

# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password')#,'First Name','Last Name','Bio')
    # date_hierarchy = 'created' 
    # search_fields = ('author')