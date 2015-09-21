from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse

from leads.models import Lead
from leads.forms import LeadForm


def index(request):
    leads = Lead.objects.filter(is_test_lead=True)

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

        return HttpResponseRedirect(reverse('leads:lead_detail', kwargs={'lead_id': lead_id}))

    else:
        return HttpResponseForbidden

def create_lead(request):

    if request.method == 'GET':
        form = LeadForm()

        return render(request, 'create_lead.html', {'form': form})

    elif request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_test_lead = True
            instance.save()

            return HttpResponseRedirect(reverse('leads:lead_detail', kwargs={'lead_id': instance.id}))

        else:
            return render(request, 'create_lead.html', {'form': form})

    else:
        return HttpResponseForbidden

def delete_lead(request, lead_id):
    lead_obj = get_object_or_404(Lead, id=lead_id)
    lead_obj.delete()

    return HttpResponseRedirect(reverse('leads:index'))