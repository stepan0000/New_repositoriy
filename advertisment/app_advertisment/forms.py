from django import forms
class AdvertismentForm(forms.Form):
    title = forms.CharField(max_length=120,widget=forms.TextInput(attrs = {'class':"form-control form-control-lg"}))
    descriptions = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(widget= forms.NumberInput(attrs = {"class":"form-control form-control-lg"}))
    trades = forms.BooleanField(required=False)
    image = forms.ImageField(widget= forms.FileInput(attrs = {"class":"form-control form-control-lg"}))