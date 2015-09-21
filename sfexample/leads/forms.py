from django import forms

from leads.models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'company', 'phone', 'mobile_phone', 'street', 'city',
                  'state', 'postal_code', 'email']