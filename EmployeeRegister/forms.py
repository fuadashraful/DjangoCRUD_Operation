from django import forms
from .models import Employee



class Employee_form(forms.ModelForm):

    class Meta:
        model=Employee
        fields=('fullName','emp_code','mobileNo','position')
        labels={
            'fullName':"Your Name",
            'emp_code':"Employee Code",
            'mobileNo':"Mobile No",
            'position':'Current Position',
        }
    def __init__(self,*args,**kwargs):
        super(Employee_form,self).__init__(*args,**kwargs)
        self.fields["position"].empty_label="Select"