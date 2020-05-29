from django import forms
from django.core import validators


# # Custome Validator
# # For checking the name start with the charecter "Z"
# def check_z(value):
#     if value[0].lower()!='z':
#         raise forms.ValidationError("Name needs to start with 'Z' ")

class Formname(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter your email again')
    text=forms.CharField(widget=forms.Textarea)

    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['email']
        vemail=all_clean_data['verify_email']

        if email != vemail:
            raise forms.ValidationError("Make sure emails are match")

    # botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher=self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher