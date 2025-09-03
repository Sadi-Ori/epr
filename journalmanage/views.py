# journalmanage/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Journal, JournalEntry
from .forms import JournalForm, JournalEntryFormSet

def journal_list(request):
    journals = Journal.objects.all().order_by('-created_at')
    paginator = Paginator(journals, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = JournalForm()

    if request.method == 'POST':
        form = JournalForm(request.POST)
        if form.is_valid():
            journal = form.save(commit=False)
            journal.save()
            return JsonResponse({'success': True, 'journal_id': journal.id})
        return JsonResponse({'success': False, 'errors': form.errors})

    return render(request, 'journalmanage/journal_list.html', {
        'page_obj': page_obj,
        'form': form
    })

def journal_approve(request):
    # This view is a placeholder for the "Journal Approve" submenu.
    # We will filter for pending journals and provide approve/reject functionality here.
    approved_journals = Journal.objects.filter(status='approved').order_by('-created_at')
    paginator = Paginator(approved_journals, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'journalmanage/journal_approve.html', {'page_obj': page_obj})

def journal_print_invoice(request, pk):
    journal = get_object_or_404(Journal, pk=pk)
    entries = journal.entries.all()
    
    total_debit = sum(entry.debit_amount for entry in entries)
    total_credit = sum(entry.credit_amount for entry in entries)

    context = {
        'journal': journal,
        'entries': entries,
        'total_debit': total_debit,
        'total_credit': total_credit,
    }
    return render(request, 'journalmanage/journal_invoice_template.html', context)