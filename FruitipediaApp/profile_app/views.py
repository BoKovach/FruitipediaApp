from django.shortcuts import render, redirect

from FruitipediaApp.fruit_app.models import FruitModel
from FruitipediaApp.profile_app.forms import CreateProfileForm, EditProfileForm
from FruitipediaApp.profile_app.models import ProfileModel


def create_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    form = CreateProfileForm()
    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    all_fruits = FruitModel.objects.count()
    profile = ProfileModel.objects.first()
    context = {
        'profile': profile,
        'posts': all_fruits,
    }
    return render(request, 'details-profile.html', context)


def edit_profile(request):
    profile = ProfileModel.objects.first()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    form = EditProfileForm(initial=profile.__dict__)
    context = {
        'profile': profile,
        'form': form,
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = ProfileModel.objects.first()
    fruits = FruitModel.objects.all()

    if request.method == 'POST':
        fruits.delete()
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
    }
    return render(request, 'delete-profile.html', context)
