from django.urls import path

from . import views

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='index'),
    path('income/', views.add_income, name='add-income'),
    path('expense/', views.add_expense, name='add-expense')
]
