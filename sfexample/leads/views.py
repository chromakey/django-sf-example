from django.core.exceptions import SuspiciousOperation
from django.shortcuts import redirect, render, get_object_or_404

from .forms import LeadForm
from .models import Lead


def index(request):
    leads = Lead.objects.filter()

    return render(request, 'index.html', {'leads': leads})


def lead_detail(request, lead_id):
    lead_obj = get_object_or_404(Lead, id=lead_id)

    return render(request, 'lead_detail.html', {'lead': lead_obj})


def edit_lead(request, lead_id):
    if request.method == 'GET':
        lead_obj = get_object_or_404(Lead, id=lead_id)
        form = LeadForm(instance=lead_obj)

        return render(request, 'edit_lead.html', {'form': form, 'lead': lead_obj})

    elif request.method == 'POST':
        lead_obj = get_object_or_404(Lead, id=lead_id)
        form = LeadForm(request.POST, instance=lead_obj)

        if form.is_valid():
            form.save()

        return redirect('leads:lead_detail', lead_id=lead_id)

    else:
        raise SuspiciousOperation


def create_lead(request):
    if request.method == 'GET':
        form = LeadForm()

        return render(request, 'create_lead.html', {'form': form})

    elif request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()

            return redirect('leads:lead_detail', lead_id=instance.id)

        else:
            return render(request, 'create_lead.html', {'form': form})

    else:
        raise SuspiciousOperation


def delete_lead(request, lead_id):
    if request.method == 'POST':
        lead_obj = get_object_or_404(Lead, id=lead_id)
        lead_obj.delete()

    return redirect('leads:index')
