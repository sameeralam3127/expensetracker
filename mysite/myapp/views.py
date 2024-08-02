from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils.timezone import now
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncWeek, TruncYear

def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('index')
    else:
        form = ExpenseForm()
    
    expenses = Expense.objects.all()
    total_sum = expenses.aggregate(Sum('amount'))['amount__sum'] or 0

    # Calculate sums for the current year, month, and week
    current_year = now().year
    current_month = now().month
    current_week = now().isocalendar()[1]

    yearly_sum = expenses.filter(date__year=current_year).aggregate(Sum('amount'))['amount__sum'] or 0
    monthly_sum = expenses.filter(date__year=current_year, date__month=current_month).aggregate(Sum('amount'))['amount__sum'] or 0
    weekly_sum = expenses.filter(date__year=current_year, date__week=current_week).aggregate(Sum('amount'))['amount__sum'] or 0

    # Prepare data for pie chart
    expense_categories = expenses.values('category').annotate(total=Sum('amount'))
    category_names = [expense['category'] for expense in expense_categories]
    category_totals = [expense['total'] for expense in expense_categories]
    
    context = {
        'expense_form': form,
        'expenses': expenses,
        'total_sum': total_sum,
        'yearly_sum': yearly_sum,
        'monthly_sum': monthly_sum,
        'weekly_sum': weekly_sum,
        'category_names': category_names,
        'category_totals': category_totals,
    }
    
    return render(request, 'myapp/index.html', context)


# View to edit an existing expense
def edit_expense(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('index')  # Redirect to the list or detail view
    else:
        form = ExpenseForm(instance=expense)
    
    return render(request, 'myapp/edit_expense.html', {'form': form})

# View to delete an expense
def delete_expense(request, pk):
    if request.method == 'POST':
        expense = get_object_or_404(Expense, pk=pk)
        expense.delete()
        messages.success(request, 'Expense deleted successfully!')
    return redirect('index')  # Redirect to the list or another appropriate view
