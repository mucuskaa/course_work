from django.contrib import admin
from .models import *
from transactions.models import Transaction, Category

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'date', 'user', 'transaction_type', 'category')
    search_fileds = ('id', 'date', 'category')
    list_filter=('date', )

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image')
    search_fileds = ('id', 'name')

admin.site.register(Transaction,TransactionAdmin)
admin.site.register(Category, CategoryAdmin)
