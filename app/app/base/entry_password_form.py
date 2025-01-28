from django import forms
from password_manager.models.entry_password import EntryPassword

class EntryPasswordForm(forms.ModelForm):

    class Meta:
        model = EntryPassword
        fields = ['website', 'website_url', 'username', 'password']