
# from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator
# from .models import Product, Godown, Dump, CostCenter
# from .forms import ProductForm, GodownForm, DumpForm, CostCenterForm

# def home(request):
#     return render(request, 'godown/home.html', {'title': 'Dashboard'})

# # --- Product Views ---
# def product_list(request):
#     products = Product.objects.all().order_by('id')
#     paginator = Paginator(products, 30)  # Show 30 products per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'godown/product_list.html', {'page_obj': page_obj})

# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm()
#     return render(request, 'godown/product_form.html', {'form': form, 'title': 'Create Product'})

# def product_edit(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'godown/product_form.html', {'form': form, 'title': 'Edit Product'})

# # --- Godown Views ---
# def godown_list(request):
#     godowns = Godown.objects.all().order_by('id')
#     paginator = Paginator(godowns, 30)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'godown/godown_list.html', {'page_obj': page_obj})

# def godown_create(request):
#     if request.method == 'POST':
#         form = GodownForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('godown_list')
#     else:
#         form = GodownForm()
#     return render(request, 'godown/godown_form.html', {'form': form, 'title': 'Create Godown'})

# def godown_edit(request, pk):
#     godown = get_object_or_404(Godown, pk=pk)
#     if request.method == 'POST':
#         form = GodownForm(request.POST, instance=godown)
#         if form.is_valid():
#             form.save()
#             return redirect('godown_list')
#     else:
#         form = GodownForm(instance=godown)
#     return render(request, 'godown/godown_form.html', {'form': form, 'title': 'Edit Godown'})

# # --- Dump Views ---
# def dump_list(request):
#     dumps = Dump.objects.all().order_by('id')
#     paginator = Paginator(dumps, 30)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'godown/dump_list.html', {'page_obj': page_obj})

# def dump_create(request):
#     if request.method == 'POST':
#         form = DumpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dump_list')
#     else:
#         form = DumpForm()
#     return render(request, 'godown/dump_form.html', {'form': form, 'title': 'Create Dump'})

# def dump_edit(request, pk):
#     dump = get_object_or_404(Dump, pk=pk)
#     if request.method == 'POST':
#         form = DumpForm(request.POST, instance=dump)
#         if form.is_valid():
#             form.save()
#             return redirect('dump_list')
#     else:
#         form = DumpForm(instance=dump)
#     return render(request, 'godown/dump_form.html', {'form': form, 'title': 'Edit Dump'})

# # --- Cost Center Views ---
# def cost_center_list(request):
#     cost_centers = CostCenter.objects.all().order_by('id')
#     paginator = Paginator(cost_centers, 30)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'godown/cost_center_list.html', {'page_obj': page_obj})

# def cost_center_create(request):
#     if request.method == 'POST':
#         form = CostCenterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('cost_center_list')
#     else:
#         form = CostCenterForm()
#     return render(request, 'godown/cost_center_form.html', {'form': form, 'title': 'Create Cost Center'})

# def cost_center_edit(request, pk):
#     cost_center = get_object_or_404(CostCenter, pk=pk)
#     if request.method == 'POST':
#         form = CostCenterForm(request.POST, instance=cost_center)
#         if form.is_valid():
#             form.save()
#             return redirect('cost_center_list')
#     else:
#         form = CostCenterForm(instance=cost_center)
#     return render(request, 'godown/cost_center_form.html', {'form': form, 'title': 'Edit Cost Center'})

# godown/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Product, Godown, Dump, CostCenter
from .forms import ProductForm, GodownForm, DumpForm, CostCenterForm

def home(request):
    return render(request, 'godown/home.html')

def product_list(request):
    products = Product.objects.all().order_by('id')
    paginator = Paginator(products, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'godown/product_list.html', {'page_obj': page_obj})

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'godown/product_form.html', {'form': form, 'title': 'Create Product'})

def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'godown/product_form.html', {'form': form, 'title': 'Edit Product'})

def godown_list(request):
    godowns = Godown.objects.all().order_by('id')
    paginator = Paginator(godowns, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'godown/godown_list.html', {'page_obj': page_obj})

def godown_create(request):
    if request.method == 'POST':
        form = GodownForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('godown_list')
    else:
        form = GodownForm()
    return render(request, 'godown/godown_form.html', {'form': form, 'title': 'Create Godown'})

def godown_edit(request, pk):
    godown = get_object_or_404(Godown, pk=pk)
    if request.method == 'POST':
        form = GodownForm(request.POST, instance=godown)
        if form.is_valid():
            form.save()
            return redirect('godown_list')
    else:
        form = GodownForm(instance=godown)
    return render(request, 'godown/godown_form.html', {'form': form, 'title': 'Edit Godown'})

def dump_list(request):
    dumps = Dump.objects.all().order_by('id')
    paginator = Paginator(dumps, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'godown/dump_list.html', {'page_obj': page_obj})

def dump_create(request):
    if request.method == 'POST':
        form = DumpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dump_list')
    else:
        form = DumpForm()
    return render(request, 'godown/dump_form.html', {'form': form, 'title': 'Create Dump'})

def dump_edit(request, pk):
    dump = get_object_or_404(Dump, pk=pk)
    if request.method == 'POST':
        form = DumpForm(request.POST, instance=dump)
        if form.is_valid():
            form.save()
            return redirect('dump_list')
    else:
        form = DumpForm(instance=dump)
    return render(request, 'godown/dump_form.html', {'form': form, 'title': 'Edit Dump'})

def cost_center_list(request):
    cost_centers = CostCenter.objects.all().order_by('id')
    paginator = Paginator(cost_centers, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'godown/cost_center_list.html', {'page_obj': page_obj})

def cost_center_create(request):
    if request.method == 'POST':
        form = CostCenterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cost_center_list')
    else:
        form = CostCenterForm()
    return render(request, 'godown/cost_center_form.html', {'form': form, 'title': 'Create Cost Center'})

def cost_center_edit(request, pk):
    cost_center = get_object_or_404(CostCenter, pk=pk)
    if request.method == 'POST':
        form = CostCenterForm(request.POST, instance=cost_center)
        if form.is_valid():
            form.save()
            return redirect('cost_center_list')
    else:
        form = CostCenterForm(instance=cost_center)
    return render(request, 'godown/cost_center_form.html', {'form': form, 'title': 'Edit Cost Center'})