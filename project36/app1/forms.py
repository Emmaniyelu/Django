from django import forms

class StudentForm(forms.Form):
    name=forms.CharField(label="StudentName",max_length=20)
    courses=(("4000","Python"),
    ("2000","Java"),
    ("1000","Oracle"))
    course=forms.ChoiceField(choices=courses)
