# # from django import forms
# # from django.contrib.auth.models import User
# # from . import models
# # from quiz import models as QMODEL
# #
# # class StudentUserForm(forms.ModelForm):
# #     class Meta:
# #         model=User
# #         fields=['first_name','last_name','username','password']
# #         widgets = {
# #         'password': forms.PasswordInput()
# #         }
# #
# # class StudentForm(forms.ModelForm):
# #     class Meta:
# #         model=models.Student
# #         fields=['address','mobile','profile_pic']
# #
# from django import forms
# from django.contrib.auth.models import User
# from . import models
#
# class StudentUserForm(forms.ModelForm):
#     # Adding email as a new field
#     email = forms.EmailField(required=True)
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'password', 'email']  # Include email in the fields list
#         widgets = {
#             'password': forms.PasswordInput()
#         }
#
# class StudentForm(forms.ModelForm):
#     # Adding date_of_birth and gender as new fields
#     date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))  # Date picker for date_of_birth
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female'),
#         ('O', 'Other'),
#     ]
#     gender = forms.ChoiceField(choices=GENDER_CHOICES)
#
#     class Meta:
#         model = models.Student
#         fields = ['address', 'mobile', 'profile_pic', 'date_of_birth', 'gender']  # Include new fields in the fields list
from django import forms
from django.contrib.auth.models import User
from . models import Student

class StudentUserForm(forms.ModelForm):
    email = forms.EmailField(required=True)  # Adding email field to the form

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']  # Include email
        widgets = {
            'password': forms.PasswordInput()
        }

class StudentForm(forms.ModelForm):
    # date_of_birth = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2100)))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=True)  # Adding gender field

    class Meta:
        model = Student
        fields = ['address', 'mobile', 'profile_pic', 'dob', 'gender']  # Include new fields
