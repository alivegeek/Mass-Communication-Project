from django import forms

from .models import Contacts, Groups

class PostForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ('firstName','lastName','phoneNumber','email','note', 'group')

class groupsForm(forms.ModelForm):

    class Meta:
        model = Groups
        fields = ('groupName','groupDesc')