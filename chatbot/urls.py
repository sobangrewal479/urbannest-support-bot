from django.urls import path

from . import views

urlpatterns = [
    path("", views.chatbot_home, name="chatbot_home"),
    path("chat/", views.chat_response, name="chat_response"),
    path("submit-lead/", views.submit_lead, name="submit_lead"),
    path("leads/", views.lead_list, name="lead_list"),
]