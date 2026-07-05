from django.http import JsonResponse
from django.shortcuts import render

from .bot_logic import get_bot_response
from .forms import LeadForm
from .models import Lead


def chatbot_home(request):
    return render(request, "chatbot/chatbot.html")


def chat_response(request):
    user_message = request.GET.get("message", "")
    bot_reply = get_bot_response(user_message)

    return JsonResponse({
        "user_message": user_message,
        "bot_reply": bot_reply,
    })


def submit_lead(request):
    if request.method != "POST":
        return JsonResponse({
            "success": False,
            "message": "Invalid request method."
        }, status=405)

    form = LeadForm(request.POST)

    if form.is_valid():
        form.save()
        return JsonResponse({
            "success": True,
            "message": "Thank you. Your inquiry has been saved. The UrbanNest team will contact you soon."
        })

    return JsonResponse({
        "success": False,
        "errors": form.errors,
    }, status=400)


def lead_list(request):
    leads = Lead.objects.all().order_by("-created_at")
    return render(request, "chatbot/leads.html", {"leads": leads})