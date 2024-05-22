from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction as trans
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Transaction, Category

from django.db.models import Q, Sum


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
        expense_transactions = Transaction.objects.filter(
            user=user, transaction_type='expense').order_by('-date')[:4]

        context['show_more_income'] = Transaction.objects.filter(
            user=user, transaction_type='income').count() > 4
        context['show_more_expense'] = Transaction.objects.filter(
            user=user, transaction_type='expense').count() > 4

        context['income_transactions'] = income_transactions
        context['expense_transactions'] = expense_transactions

        categories_income = Category.objects.filter(type_category='income')
        context['categories_income'] = categories_income

        categories_expense = Category.objects.filter(type_category='expense')
        context['categories_expense'] = categories_expense

        tickers = range(1, 10)
        context['tickers'] = tickers

        expense = Transaction.objects.filter(
            user=user, transaction_type='expense').order_by('-amount')
        labels = [expense.category.name for expense in expense]
        unique_labels = list(set(labels))
        data = {label: str(sum(expense.amount for expense in expense if expense.category.name == label)) for label in
                unique_labels}
        sorted_data = dict(
            sorted(data.items(), key=lambda x: float(x[1]), reverse=True))
        context['qs'] = {
            'labels': list(sorted_data.keys()),
            'data': list(sorted_data.values()),
        }

        income = Transaction.objects.filter(
            user=user, transaction_type='income').order_by('-amount')
        inc_labels = [income.category.name for income in income]
        inc_unique_labels = list(set(inc_labels))
        inc_data = {label: str(sum(income.amount for income in income if income.category.name == label)) for label in
                    inc_unique_labels}
        inc_sorted_data = dict(
            sorted(inc_data.items(), key=lambda x: float(x[1]), reverse=True))
        context['incqs'] = {
            'labels': list(inc_sorted_data.keys()),
            'data': list(inc_sorted_data.values()),
        }

        total_expense = \
        Transaction.objects.filter(user=user, transaction_type='expense').aggregate(total_expense=Sum('amount'))[
            'total_expense'] or 0
        total_income = \
        Transaction.objects.filter(user=user, transaction_type='income').aggregate(total_income=Sum('amount'))[
            'total_income'] or 0

        context['totqs'] = {
            'labels': ['Надходження', 'Витрати', ],
            'data': [str(total_income), str(total_expense)],
        }

        context['has_income'] = income_transactions.exists()
        context['has_expense'] = expense_transactions.exists()
        context['has_data'] = context['has_income'] or context['has_expense']

        return context


class TransactionIncomeListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/income_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user, transaction_type='income').order_by('-date').all()


class TransactionExpenseListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/expense_list.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user, transaction_type='expense').order_by('-date').all()


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

        transaction_type = 'expense'
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
