from django.contrib import admin
from django.contrib.auth import get_user_model

class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'nickname', 'wallet', 'email', 'date_of_registration')
    search_fileds=('id', 'username', 'nickname', 'date_of_registration')
    list_filter = ('date_of_registration',)

User = get_user_model()

admin.site.register(User, UserAdmin)
