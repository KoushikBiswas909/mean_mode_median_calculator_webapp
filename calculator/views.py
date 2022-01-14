from operator import mod
from django.shortcuts import render
from statistics import mean, median, mode
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.


def input_data(request):
    return render(request, 'calculator/input.html')


def add(request):
    input_list = request.GET["list"]
    user_list = input_list.split()

    for i in range(len(user_list)):
        user_list[i] = float(user_list[i])

    # Calculating Mean value
    mean_value = mean(user_list)
    # Calculating Median value
    median_value = median(user_list)
    # Calculating Mode value
    mode_value = mode(user_list)

    # Three values combained in a Data Structure List
    mean_median_mode_result_list = [mean_value, median_value, mode_value]

    return render(request, 'calculator/result.html', {"result": mean_median_mode_result_list})


# User Register
def register(request):
    form = UserCreationForm
    if request.method == "POST":
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, "User has been registered.")
        else:
            messages.warning(request, "Enter details again")
    return render(request, "registration/register.html", {"form": form})
