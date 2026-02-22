from .models import Employee
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm

def employees(request):
    employees = Employee.objects.all()
    
    return render(request, "employees.html", {"employees": employees})

def create_employee(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("employees")
    else:
        form = EmployeeForm()
    
    return render(request, "employee-form.html", {"form": form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == "POST":
        employee.delete()
    
    return redirect("employees")
