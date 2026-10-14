from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and subject and message:
            messages.success(
                request,
                "Thank you! Your message has been received."
            )
            return redirect("contact")

        messages.error(request, "Please fill in all the fields.")

    return render(request, "core/contact.html")
