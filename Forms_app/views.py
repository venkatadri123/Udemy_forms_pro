from django.shortcuts import render
from Forms_app import forms

# Create your views here.
def index(request):
    return render(request,'forms_app/index.html')

def form_name(request):
    form=forms.Formname()
    if request.method=='POST':
        form=forms.Formname(request.POST)
        if form.is_valid():
            # Do something code
            print("VALIDATION SUCCESS!")
            print("name"+form.cleaned_data['name'])
            print("Email:"+form.cleaned_data['email'])
            print("Text:"+form.cleaned_data['text'])
    return render(request,'forms_app/forms.html',{'form':form})
