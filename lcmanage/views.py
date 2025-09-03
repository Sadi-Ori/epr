# from django.shortcuts import render, redirect, get_object_or_404
# from django.core.paginator import Paginator
# from .models import Type, Consignee_name, Consingnee_owner_name, Contact_number, Consignee_address, Registration_number
# from .forms import Type, Consignee_name, Consingnee_owner_name, Contact_number, Consignee_address, Registration_number

# def home(request):
#     return render(request, 'lcmanage/home.html', {'title': 'Dashboard'})

# # --- Product Views ---
# def Consignee_list(request):
#     consigneee = Consigneee.objects.all().order_by('id')
#     paginator = Paginator(consigneee, 30)  # Show 30 products per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'lcmanage/consignee_list.html', {'page_obj': page_obj})

# def consignee_create(request):
#     if request.method == 'POST':
#         form = Consignee(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('consigneee_list')
#     else:
#         form = Consignee()
#     return render(request, 'lcmanage/consignee_form.html', {'form': form, 'title': 'Create Consignee'})

# def consignee_edit(request, pk):
#     consignee = get_object_or_404(Consignee, pk=pk)
#     if request.method == 'POST':
#         form = ConsigneeForm(request.POST, instance=consignee)
#         if form.is_valid():
#             form.save()
#             return redirect('consignee_list')
#     else:
#         form = ConsigneeForm(instance=consignee)
#     return render(request, 'lcmanage/consignee_form.html', {'form': form, 'title': 'Edit Consignee'})

# # # --- Godown Views ---
# # def godown_list(request):
# #     godowns = Godown.objects.all().order_by('id')
# #     paginator = Paginator(godowns, 30)
# #     page_number = request.GET.get('page')
# #     page_obj = paginator.get_page(page_number)
# #     return render(request, 'godown/godown_list.html', {'page_obj': page_obj})

# # def godown_create(request):
# #     if request.method == 'POST':
# #         form = GodownForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('godown_list')
# #     else:
# #         form = GodownForm()
# #     return render(request, 'godown/godown_form.html', {'form': form, 'title': 'Create Godown'})

# # def godown_edit(request, pk):
# #     godown = get_object_or_404(Godown, pk=pk)
# #     if request.method == 'POST':
# #         form = GodownForm(request.POST, instance=godown)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('godown_list')
# #     else:
# #         form = GodownForm(instance=godown)
# #     return render(request, 'godown/godown_form.html', {'form': form, 'title': 'Edit Godown'})

# # # --- Dump Views ---
# # def dump_list(request):
# #     dumps = Dump.objects.all().order_by('id')
# #     paginator = Paginator(dumps, 30)
# #     page_number = request.GET.get('page')
# #     page_obj = paginator.get_page(page_number)
# #     return render(request, 'godown/dump_list.html', {'page_obj': page_obj})

# # def dump_create(request):
# #     if request.method == 'POST':
# #         form = DumpForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('dump_list')
# #     else:
# #         form = DumpForm()
# #     return render(request, 'godown/dump_form.html', {'form': form, 'title': 'Create Dump'})

# # def dump_edit(request, pk):
# #     dump = get_object_or_404(Dump, pk=pk)
# #     if request.method == 'POST':
# #         form = DumpForm(request.POST, instance=dump)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('dump_list')
# #     else:
# #         form = DumpForm(instance=dump)
# #     return render(request, 'godown/dump_form.html', {'form': form, 'title': 'Edit Dump'})

# # # --- Cost Center Views ---
# # def cost_center_list(request):
# #     cost_centers = CostCenter.objects.all().order_by('id')
# #     paginator = Paginator(cost_centers, 30)
# #     page_number = request.GET.get('page')
# #     page_obj = paginator.get_page(page_number)
# #     return render(request, 'godown/cost_center_list.html', {'page_obj': page_obj})

# # def cost_center_create(request):
# #     if request.method == 'POST':
# #         form = CostCenterForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('cost_center_list')
# #     else:
# #         form = CostCenterForm()
# #     return render(request, 'godown/cost_center_form.html', {'form': form, 'title': 'Create Cost Center'})

# # def cost_center_edit(request, pk):
# #     cost_center = get_object_or_404(CostCenter, pk=pk)
# #     if request.method == 'POST':
# #         form = CostCenterForm(request.POST, instance=cost_center)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('cost_center_list')
# #     else:
# #         form = CostCenterForm(instance=cost_center)
# #     return render(request, 'godown/cost_center_form.html', {'form': form, 'title': 'Edit Cost Center'})

# lcmanage/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Consignee, LC
from .forms import ConsigneeForm, LCForm, LCUpdateForm

def consignee_list(request):
    consignees = Consignee.objects.all().order_by('id')
    paginator = Paginator(consignees, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = ConsigneeForm()
    return render(request, 'lcmanage/consignee_list.html', {'page_obj': page_obj, 'form': form})

def consignee_create(request):
    if request.method == 'POST':
        form = ConsigneeForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})

def consignee_edit(request, pk):
    consignee = get_object_or_404(Consignee, pk=pk)
    if request.method == 'POST':
        form = ConsigneeForm(request.POST, instance=consignee)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})

def lc_list(request):
    lcs = LC.objects.all().order_by('id')
    paginator = Paginator(lcs, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    lc_form = LCForm()
    lc_update_form = LCUpdateForm()

    if request.method == 'POST' and 'create_lc' in request.POST:
        lc_form = LCForm(request.POST)
        if lc_form.is_valid():
            lc_form.save()
            return redirect('lcmanage:lc_list')

    return render(request, 'lcmanage/lc_list.html', {
        'page_obj': page_obj,
        'lc_form': lc_form,
        'lc_update_form': lc_update_form
    })

def lc_update(request, pk):
    lc = get_object_or_404(LC, pk=pk)
    if request.method == 'POST':
        form = LCUpdateForm(request.POST, instance=lc)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'errors': 'Invalid request method.'})