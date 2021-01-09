from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    mail = forms.EmailField()
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form_control'}))
    sender = forms.EmailField(widget=forms.TextInput(attrs={'size':'40','class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
