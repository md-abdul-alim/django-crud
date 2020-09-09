from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee
# Create your views here.


def employee_form(request, id=0):
    # if block for showing data for updateing
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(instance=employee)
        context = {
            'form': form,
        }
        return render(request, "employee/employee_form.html", context)
    #else block for insert and update
    else:
        if id == 0:
            #in insert time there is no id.so this block works for inserting post data
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(id=id)
            form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('/list/')


def employee_list(request):
    employee_list = Employee.objects.all()
    context = {
        'employee_list': employee_list
    }
    return render(request, "employee/employee_list.html", context)


def employee_delete(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/list/')
