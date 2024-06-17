from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from userauths.models import User, Profile
from userauths.forms import UserRegisterForm



def registerView(request):
    if request.user.is_authenticated:
        messages.warning(request, f"You are already logged in")
        return redirect("hotel:index")

    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        full_name = form.changed_data.get("full_name")
        phone = form.changed_data.get("phone")
        email = form.changed_data.get("email")
        password = form.changed_data.get("password")

        user = authenticate(email=email, password=password)
        login(request, user)

        messages.success(request, f"Hey {full_name}, your account has been created successfully")

        profile = Profile.objects.get(user=request.user)
        profile.full_name = full_name
        profile.phone = phone
        profile.save()

        return redirect("hotel:index")


    context = {
        "form": form
    }
    return render(request, "userauths/sign-up.html", context)