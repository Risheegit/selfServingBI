from django import forms
from .models import DropdownChoice

class DropdownForm(forms.ModelForm):
    OPTIONS = [('default', 'Default'), ('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')]

    dropdown1 = forms.ChoiceField(choices=OPTIONS, required=True, initial='default', label="Dropdown 1")
    dropdown2 = forms.ChoiceField(choices=OPTIONS, required=True, initial='default', label="Dropdown 2")
    dropdown3 = forms.ChoiceField(choices=OPTIONS, required=True, initial='default', label="Dropdown 3")
    dropdown4 = forms.ChoiceField(choices=OPTIONS, required=True, initial='default', label="Dropdown 4")

    class Meta:
        model = DropdownChoice
        fields = ['dropdown1', 'dropdown2', 'dropdown3', 'dropdown4']
