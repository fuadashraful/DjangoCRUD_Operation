
from django.conf.urls import url
from django.urls import path
from . import views
urlpatterns = [
  url(r'^home/$',views.EmployeeForm,name="employeeForm"), #get4 and post request for insert operation
  url(r'^list/$',views.EmployeeList,name="employeeList"),  # get request to retrive and display
  path('home/<int:id>',views.EmployeeForm,name="employee_update"),  #get and post for  update operation
  path('delete/<int:id>',views.EmployeeDelete,name="employee_delete"),

]
