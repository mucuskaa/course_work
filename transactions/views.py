from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction as trans
from django.shortcuts import redirect
from django.views.generic import ListView

from .models import Transaction, Category


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'transactions/index.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user

        categories = Category.objects.all()
        context['categories'] = categories

        tickers = range(1, 10)
        context['tickers'] = tickers

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
