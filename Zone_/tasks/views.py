from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Form definition
class NTF(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)


def index(request):
    # Fix: Use 'request.session' (singular)
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {"tasks": request.session["tasks"]})


def add(request):
    if request.method == "POST":
        form = NTF(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]

            # Ensure session is initialized
            if "tasks" not in request.session:
                request.session["tasks"] = []

            # Append to the session list and mark it as modified
            request.session["tasks"] += [task]

            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})

    return render(request, "tasks/add.html", {"form": NTF()})
