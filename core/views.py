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

        form_data = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message,
        }

        errors = []

        if not name or len(name) > 100:
            errors.append("Enter a name of no more than 100 characters.")

        if not email or len(email) > 254 or "@" not in email:
            errors.append("Enter a valid email address.")

        if not subject or len(subject) > 150:
            errors.append("Enter a subject of no more than 150 characters.")

        if not message or len(message) > 5000:
            errors.append("Enter a message of no more than 5,000 characters.")

        if errors:
            return render(
                request,
                "core/contact.html",
                {
                    "form_data": form_data,
                    "form_errors": errors,
                },
            )

        messages.success(
            request,
            f"Thank you, {name}! Your form was submitted successfully."
        )
        return redirect("core:contact")

    return render(request, "core/contact.html")