from django import forms
from password_manager.models.entry_password import EntryPassword

class SearchWebSiteForm(forms.ModelForm):
    class Meta:
        model = EntryPassword
        fields = ['website_name']