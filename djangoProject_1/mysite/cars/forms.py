from django import forms
from .models import Review
from django.forms import ModelForm

#class Review_Form(forms.Form):
    #first_name = forms.CharField(label='First_name', max_length=100)
    #last_name = forms.CharField(label='Last_name',max_length=100)
    #email = forms.EmailField(label="Email")
    #review = forms.CharField(label='please write your review here', widget=forms.Textarea(attrs={'class':'myform','rows':'2', 'cols':'4'}))

class Review_Form(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" #pass in all model fields as form fields

        labels={
            'first_name' : 'YOUR FIRST NAME',
            'last_name':'Last Name',
            'stars' : 'rating'
        }

        error_messages = {
            'stars':{
                'min_value':'Yo! Min value is 1',
                'max_value':'Yo! Yo max value is 5'
            }
        }