from .models import *
from django import forms

class authorForm(forms.ModelForm):
    fname = forms.CharField(max_length=255, required= True, widget=forms.TextInput(attrs={'class':'border rounded-md text-sm outline-none lg:px-4 px-2 lg:py-3 py-0p6rem placeholder:text-A1A1A1 text-101928 focus:border-205a42 ease-in transition-all focus:border-l-8  bg-transparent', 'placeholder':'Enter your first name', 'autocomplete':'off'}))
    lname = forms.CharField(max_length=255, required = True, widget=forms.TextInput(attrs={'class':'border rounded-md text-sm outline-none lg:px-4 px-2 lg:py-3 py-0p6rem placeholder:text-A1A1A1 text-101928 focus:border-205a42 ease-in transition-all focus:border-l-8  bg-transparent', 'placeholder':'Enter your last name', 'autocomplete':'off'}))
    email = forms.EmailField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'border rounded-md text-sm outline-none lg:px-4 px-2 lg:py-3 py-0p6rem placeholder:text-A1A1A1 text-101928 focus:border-205a42 ease-in transition-all focus:border-l-8  bg-transparent', 'placeholder':'Enter your Email', 'autocomplete':'off'}))
    
    def clean_fName(self, *args, **kwargs):
        fname = self.cleaned_data.get('fname')
        if not fname:
            raise forms.ValidationError("First name is required")
        return fname

    def clean_lName(self, *args, **kwargs):
        lname = self.cleaned_data.get('lname')
        if not lname:
            raise forms.ValidationError("First name is required")
        return lname

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required")
        return email
    
    class Meta:
        model = Author
        fields = '__all__'
        exclude = ['created']


class blogForm(forms.ModelForm):
    title = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'border rounded-md text-sm outline-none lg:px-4 px-2 lg:py-3 py-0p6rem placeholder:text-A1A1A1 text-101928 focus:border-205a42 ease-in transition-all focus:border-l-8  bg-transparent', 'placeholder':'Enter your first name', 'autocomplete':'off'}))
    des = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'border rounded-md text-sm outline-none lg:px-4 px-2 lg:py-3 py-0p6rem placeholder:text-A1A1A1 text-101928 focus:border-205a42 ease-in transition-all focus:border-l-8  bg-transparent', 'placeholder':'Enter your last name', 'autocomplete':'off'}))
    class Meta:
        model = Blog
        fields = '__all__'
        exclude = ['created']

class schoolForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'border rounded-md text-sm outline-none lg:px-4 px-2 lg:py-3 py-0p6rem placeholder:text-A1A1A1 text-101928 focus:border-205a42 ease-in transition-all focus:border-l-8  bg-transparent', 'placeholder':'Enter School Name: ', 'autocomplete':'off'}))
    address = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class':'border rounded-md text-sm outline-none lg:px-4 px-2 lg:py-3 py-0p6rem placeholder:text-A1A1A1 text-101928 focus:border-205a42 ease-in transition-all focus:border-l-8  bg-transparent', 'placeholder':'Enter Address: ', 'autocomplete':'off'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'minlength':"8",'maxlength':"12",'class':'pl-2 outline-none w-4ch text-sm w-full flex-1','placeholder':'enter username', 'placeholder':'Enter phone number: ', 'required':'true','type':'number', 'autocomplete':'off'}))

    class Meta:
        model = School
        fields = '__all__'
        exclude = ['created']