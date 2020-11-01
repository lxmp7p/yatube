from django.shortcuts import render, redirect
from .forms import CreationForm


def registration(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("../../auth/login")
    form = CreationForm
    return render(request, "registration/register.html", {"form": form})