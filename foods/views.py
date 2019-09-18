from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.models import User
from .forms import FoodForm

# Create your views here.
def home(request):
    pass
    # foods = Food.objects.all()
    return render(request, 'foods/home.html')


def food_new(request):
    if request.method == "POST":
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food = form.save(commit=False)
            # food.posted_by = request.user
            food.posted_by = User.objects.get(username='dfrogoso')
            food.save()

    else:
        form = FoodForm()
    return render(request, 'foods/food_edit.html', { 'form': form })
