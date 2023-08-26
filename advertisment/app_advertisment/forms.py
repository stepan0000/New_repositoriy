from django import forms
from jsonschema import ValidationError
from .models import Advertisment

# class AdvertismentForm(forms.Form):
#     title = forms.CharField(max_length= 120,widget=forms.TextInput(attrs = {"class":"form-control form-control-lg"}))
#     descriptions = forms.CharField(widget=forms.Textarea(attrs = {"class":"form-control form-control-lg"}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs = {"class":"form-control form-control-lg"}))
#     trades = forms.BooleanField(required= False)
#     image = forms.ImageField(widget=forms.FileInput(attrs = {"class":"form-control form-control-lg"}))

class AdvertismentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['descriptions'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['trades'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Advertisment
        fields = ("title", "descriptions", "image", "price", "trades")

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
        return title