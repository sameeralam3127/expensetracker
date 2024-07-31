from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import ExpenseForm
from .models import Expense

# View to list all expenses and handle the creation of new expenses
def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('index')  # Redirect to avoid form re-submission on refresh
    else:
        form = ExpenseForm()
    
    expenses = Expense.objects.all()
    return render(request, 'myapp/index.html', {'expense_form': form, 'expenses': expenses})

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
