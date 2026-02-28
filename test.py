"""
This is a basic django page for playing around to test git conflicts
"""

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.http import require_http_methods


# 1️⃣ Basic function-based view
def home(request):
    return HttpResponse("Hello, this is the home page.")


# 2️⃣ Template rendering view
def dashboard(request):
    context = {
        "username": "Aiden",
        "notifications": 3
    }
    return render(request, "dashboard.html", context)


# 3️⃣ JSON API-style view
@require_http_methods(["GET"])
def api_status(request):
    data = {
        "status": "success",
        "message": "API is working"
    }
    return JsonResponse(data)


# 4️⃣ Basic form handling (POST + GET)
@require_http_methods(["GET", "POST"])
def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        # Normally you'd save to DB here
        print(f"Received contact form from {name} ({email})")

        return redirect("home")

    return render(request, "contact.html")


# 5️⃣ Class-Based View example
class ProfileView(View):
    def get(self, request):
        return render(request, "profile.html")

    def post(self, request):
        bio = request.POST.get("bio")
        print(f"Updated bio: {bio}")
        return redirect("profile")
