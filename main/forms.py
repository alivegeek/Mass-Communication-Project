from django import forms
from main.models import *
from django.db import models
from django.contrib.auth.models import Group

class PostForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = ('firstName','lastName','phoneNumber','email','note', 'group')

class Groups(forms.ModelForm):

    class Meta:
        model = Groups
        fields = ('groupName','groupDesc')

class Users_to_groups_form(forms.ModelForm):

    OPTIONS = []
    # groups = forms.ModelMultipleChoiceField(queryset=Groups.objects.all(), widget=forms.CheckboxSelectMultiple)

    # Groups = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=options)
