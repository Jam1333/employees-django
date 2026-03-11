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

def update_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        
        if form.is_valid():
            employee.surname = form.cleaned_data["surname"]
            employee.name = form.cleaned_data["name"]
            employee.patronymic = form.cleaned_data["patronymic"]
            employee.position = form.cleaned_data["position"]
            
            employee.save()
            
            return redirect("employees")
    else:
        form = EmployeeForm({
            "surname": employee.surname, 
            "name": employee.name, 
            "patronymic": employee.patronymic,
            "position": employee.position,
        })
    
    return render(request, "employee-update-form.html", {"form": form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    
    if request.method == "POST":
        employee.delete()
    
    return redirect("employees")
