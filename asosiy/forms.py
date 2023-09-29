from django import forms
from .models import *
class TalabaForm(forms.Form):
    i = forms.CharField(label="Ism", max_length=30, min_length=3)
    k = forms.IntegerField(label="Kurs", max_value=4, min_value=1)
    k_s = forms.IntegerField(label="Kitoblar_soni")

class MuallifForm(forms.Form):
    ism = forms.CharField()
    jins = forms.CharField()
    kitob_soni = forms.IntegerField()
    tugilgan_yil = forms.DateField()
    tirik = forms.BooleanField()

class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields = "__all__"

class MuallifModelForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = "__all__"

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"

class AdminForm(forms.Form):
    ism = forms.CharField()
    ish_vaqti = forms.CharField()