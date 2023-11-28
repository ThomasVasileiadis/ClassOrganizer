from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'last_name', 'phone', 'english_level', 'obligation_name', 'obligation_datetime']

    def clean_obligation_datetime(self):
        obligation_datetime = self.cleaned_data.get('obligation_datetime')
        if not obligation_datetime:
            return None  # return None if obligation_datetime is empty
        return obligation_datetime