from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# Create your views here.
def about_me(request):
    """
    Renders the about page
    """

    if request.method == "POST":
        collaborate_from = CollaborateForm(data=request.POST)
        if collaborate_from.is_valid():
            collaborate_from.save()
            messages.add_message(request, messages.SUCCESS,
            "Collaboration request received! I endeavor to respond in 2 working days.")


    about = About.objects.all().order_by('-updated_on').first()
    collaborate_form = CollaborateForm()
        

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )