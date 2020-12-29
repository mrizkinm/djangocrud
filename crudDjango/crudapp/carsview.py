from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cars
from .forms import CarsForm
from django.views.generic import ListView, DetailView

class IndexView(ListView):
    template_name = 'cars/index.html'
    context_object_name = 'cars_list'

    def get_queryset(self):
        return Cars.objects.all()

class CarsDetailView(DetailView):
    model = Cars
    template_name = 'cars/detail.html'

def create(request):
    if request.method == 'POST':
        form = CarsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = CarsForm()

    return render(request,'cars/create.html',{'form': form})

def detail(request, pk, template_name='cars/detail.html'):
    cars = get_object_or_404(Cars, pk=pk)
    form = CarsForm(request.POST or None, instance=cars)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def edit(request, pk, template_name='cars/edit.html'):
    cars = get_object_or_404(Cars, pk=pk)
    form = CarsForm(request.POST or None, instance=cars)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form':form})

def delete(request, pk, template_name='cars/confirm_delete.html'):
    cars = get_object_or_404(Cars, pk=pk)
    if request.method=='POST':
        cars.delete()
        return redirect('index')
    return render(request, template_name, {'object':cars})