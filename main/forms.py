from django import forms
from .models import News,Student

class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'

class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

