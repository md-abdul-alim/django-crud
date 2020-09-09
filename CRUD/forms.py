
from django import forms

from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'mobile', 'emp_id', 'position')
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'emp_id': 'EMP. ID'
        }

        # fields='__all__'
    #this function is to add "select" to the position dropdown box
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "Select"
        #kono field ke required false kora
        self.fields['mobile'].required = False