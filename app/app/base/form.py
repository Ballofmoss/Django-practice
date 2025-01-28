from django import forms

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
