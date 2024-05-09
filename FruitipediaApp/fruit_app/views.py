from django.shortcuts import render, redirect

from FruitipediaApp.fruit_app.forms import FruitModelForm, DeleteFruitModelForm
from FruitipediaApp.fruit_app.models import FruitModel
from FruitipediaApp.profile_app.models import ProfileModel


def index(request):
    profile = ProfileModel.objects.all().first()
    context = {
        'profile': profile
    }
    return render(request, 'index.html', context)


def dashboard(request):
    profile = ProfileModel.objects.first()
    fruits = FruitModel.objects.all()
    context = {
        'fruits': fruits,
        'profile': profile,
    }

    return render(request, 'dashboard.html', context)


def create_fruit(request):
    if request.method == 'POST':
        form = FruitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = FruitModelForm()
    context = {
        'form': form,
        'profile': ProfileModel.objects.first(),
    }
    return render(request, 'create-fruit.html', context)


def fruit_details(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    context = {
        'fruit': fruit,
        'profile': ProfileModel,
    }
    return render(request, 'details-fruit.html', context)


def edit_fruit(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = FruitModelForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = FruitModelForm(initial=fruit.__dict__)
    context = {
        'profile': ProfileModel,
        'form': form,
        'fruit': fruit,
    }
    return render(request, 'edit-fruit.html', context)


def delete_fruit(request, pk):
    fruit = FruitModel.objects.get(pk=pk)
    if request.method == 'POST':
        fruit.delete()
        return redirect('dashboard')

    form = DeleteFruitModelForm(initial=fruit.__dict__)
    context = {
        'form': form,
        'profile': ProfileModel,
        'fruit': fruit,
    }
    return render(request, 'delete-fruit.html', context)
