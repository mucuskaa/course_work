from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction as trans
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Transaction, Category


from django.db.models import Q


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/index.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        # This is now unused but left here if needed for other purposes
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user

        income_transactions = Transaction.objects.filter(
            user=user, transaction_type='income').order_by('-date')[:4]
        expenses_transactions = Transaction.objects.filter(
            user=user, transaction_type='expenses').order_by('-date')[:4]

        context['show_more_income'] = Transaction.objects.filter(
            user=user, transaction_type='income').count() > 4
        context['show_more_expenses'] = Transaction.objects.filter(
            user=user, transaction_type='expenses').count() > 4

        context['income_transactions'] = income_transactions
        context['expenses_transactions'] = expenses_transactions

        categories = Category.objects.all()
        context['categories'] = categories

        tickers = range(1, 10)
        context['tickers'] = tickers

        # Отримуємо всі витрати користувача
        expenses = Transaction.objects.filter(user=user, transaction_type='expenses').all()

        # Створюємо список міток (назв категорій) для кожної витрати
        labels = [expense.category.name for expense in expenses]

        # Отримуємо унікальні назви категорій
        unique_labels = list(set(labels))

        # Побудова словника, де ключі - це назви категорій, а значення - це суми витрат для кожної категорії
        data = {label: sum(expense.amount for expense in expenses if expense.category.name == label) for label in
                unique_labels}

        context['qs'] = {
            'labels': list(data.keys()),  # Перетворюємо ключі словника у список міток
            'data': list(data.values()),  # Перетворюємо значення словника у список сум витрат
        }

        return context


@login_required
@trans.atomic
def add_income(request):
    if request.POST:
        amount = float(request.POST['income-amount'])
        user = request.user
        category = request.POST['income-category']

        category = Category.objects.filter(name=category).first()

        transaction_type = 'income'

        user.wallet += amount

        Transaction.objects.create(
            amount=amount,
            user=user,
            category=category,
            transaction_type=transaction_type
        )
        user.save()

    return redirect('index')


@login_required
@trans.atomic
def add_expense(request):
    if request.POST:
        amount = float(request.POST['expense-amount'])
        user = request.user
        category = request.POST['expense-category']

        category = Category.objects.filter(name=category).first()

        transaction_type = 'expenses'
        if user.wallet < amount:
            return redirect('index')

        Transaction.objects.create(
            amount=amount,
            user=user,
            category=category,
            transaction_type=transaction_type
        )
        user.wallet -= amount
        user.save()

    return redirect('index')
