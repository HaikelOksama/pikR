from django.forms import ModelForm
from django import forms
from .models import PikR, LaporanKegiatan, Anggota

from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper

class PikForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
    
    class Meta:
        model = PikR
        fields = ['nama', 'deskripsi']
        widgets = {
            'deskripsi': forms.Textarea(
            )
        }
    

class KNolForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
    
    class Meta:
        model = PikR
        fields = ['fileK0']   

class LaporanPikForm(ModelForm):
     
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))   
          
    class Meta:
        model = LaporanKegiatan
        fields = '__all__'
        exclude = ['pik']
        widgets = {
            'tanggal': forms.DateTimeInput(
                attrs={
                    'type' : 'date'
                }
            ),
            'deskripsi': forms.Textarea(
            )
        }

class AnggotaPikForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))   
    
    class Meta:
        model = Anggota
        fields = '__all__'
        exclude = ['pik']