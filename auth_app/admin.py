from django.contrib import admin
from django.contrib.auth import get_user_model

admin.site.site_header = 'Адмін панель'

class UserAdmin(admin.ModelAdmin):
    list_display=('id', 'username', 'wallet', 'email', 'date_of_registration')
    search_fileds=('id', 'username', 'date_of_registration')
    list_filter = ('date_of_registration',)

User = get_user_model()

admin.site.register(User, UserAdmin)
