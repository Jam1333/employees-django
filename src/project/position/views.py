from django.shortcuts import get_object_or_404, render, redirect
from .models import Position
from .forms import PositionForm

def positions(request):
    positions = Position.objects.all()
    
    return render (request, "positions.html", {"positions": positions})

def create_position(request):
    if request.method == "POST":
        form = PositionForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("positions")
    else:
        form = PositionForm()
    
    return render(request, "position-form.html", {"form": form})

def delete_position(request, pk):
    position = get_object_or_404(Position, pk=pk)
    
    if request.method == "POST":
        position.delete()
    
    return redirect("positions")
