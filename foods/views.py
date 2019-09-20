from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.models import User
from .forms import FoodForm
from django.contrib import auth


# Create your views here.
def home(request):
    foods = Food.objects.all().order_by('-created')
    return render(request, 'foods/home.html', {'foods':foods})

def companybg(request):
    return render(request, 'foods/companybg.html')

def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            # food.posted_by = request.user
            food.posted_by = User.objects.get(username='dfrogoso')
            food.save()
        return redirect('home')

    else:
        form = FoodForm()
    return render(request, 'foods/food_edit.html', { 'form': form })

def food_edit(request, pk):
    get = Food.objects.get(id=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES, instance=get)
        if form.is_valid():
            food = form.save(commit=True)
            food.save()
        return redirect('home')
    else:
        form = FoodForm(instance=get)
    return render(request, 'foods/food_edit.html', {'form': form, 'edit': True})