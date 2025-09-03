# purchasemanage/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Supplier, Purchase
from .forms import SupplierForm, PurchaseForm

def supplier_list(request):
    suppliers = Supplier.objects.all().order_by('id')
    paginator = Paginator(suppliers, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = SupplierForm()
    return render(request, 'purchasemanage/supplier_list.html', {'page_obj': page_obj, 'form': form})

def supplier_create(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})

def supplier_edit(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})

def purchase_create_list(request):
    purchases = Purchase.objects.filter(status='pending').order_by('-date')
    paginator = Paginator(purchases, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = PurchaseForm()

    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            # Fetch contact and address from selected supplier
            supplier = purchase.supplier
            purchase.contact = supplier.contact
            purchase.address = supplier.address
            purchase.save()
            return redirect('purchasemanage:purchase_create')
    
    return render(request, 'purchasemanage/purchase_create.html', {
        'page_obj': page_obj,
        'form': form,
        'title': 'Purchase Create'
    })

def leaf_purchase_audit(request):
    purchases = Purchase.objects.filter(status='pending').order_by('-date')
    paginator = Paginator(purchases, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'purchasemanage/leaf_purchase_audit.html', {'page_obj': page_obj})

def leaf_purchase_approve(request):
    purchases = Purchase.objects.filter(status='approved').order_by('-date')
    paginator = Paginator(purchases, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'purchasemanage/leaf_purchase_approve.html', {'page_obj': page_obj})