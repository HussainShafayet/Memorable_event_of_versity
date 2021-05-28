from django import forms
from django.forms import ModelForm
from .models import Institute_info, Versity_life_cycle
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class Institute_info_Form(forms.ModelForm):
    class Meta:
        model = Institute_info
        fields = [
            'name','dept','session','public'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Institute_info_Form, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super(Institute_info_Form, self).clean()

        if Institute_info.objects.filter(user=self.user):
            raise forms.ValidationError('User already exists.')
        return self.cleaned_data


class Cycle_Form(forms.ModelForm):
    event=forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Versity_life_cycle
        fields = [
            'institute','year','semester','event','public'
        ]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Cycle_Form, self).__init__(*args, **kwargs)
        self.fields['institute'].queryset=Institute_info.objects.filter(user=self.user)


    