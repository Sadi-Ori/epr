# accounting/views.py
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from .models import Account
from .forms import AccountForm

def account_list(request):
    accounts = Account.objects.all().order_by('id')
    form = AccountForm()
    
    ex_type = request.GET.get('ex_type')
    status = request.GET.get('status')
    keyword = request.GET.get('keyword')

    if ex_type:
        accounts = accounts.filter(ex_type=ex_type)
    
    if status:
        accounts = accounts.filter(account_status=status)
    
    if keyword:
        accounts = accounts.filter(
            Q(account_id__icontains=keyword) |
            Q(account_title__icontains=keyword) |
            Q(contact_number__icontains=keyword)
        )

    paginator = Paginator(accounts, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    ex_type_choices = Account.EX_TYPE_CHOICES
    status_choices = Account.STATUS_CHOICES

    return render(request, 'accounting/account_list.html', {
        'page_obj': page_obj,
        'form': form,
        'ex_type_choices': ex_type_choices,
        'status_choices': status_choices,
    })

def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})

def account_edit(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=account)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})

def account_delete(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        account.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})