from django import forms


class StudentForm(forms.Form):
    name=forms.CharField(label="StudentName",max_length=20)
    c1=forms.BooleanField(label="Python",required=False)
    c2=forms.BooleanField(label="Java",required=False)
    c3=forms.BooleanField(label="Oracle",required=False)
