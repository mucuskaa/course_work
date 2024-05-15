from django.urls import path

from . import views

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='index'),
    path('income/', views.add_income, name='add-income'),
    path('expense/', views.add_expense, name='add-expense'),
    path('all-incomes/', views.TransactionIncomeListView.as_view(), name='all-income'),
    path('all-expenses/', views.TransactionExpenseListView.as_view(), name='all-expense'),
]
