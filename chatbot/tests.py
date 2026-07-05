from django.test import TestCase
from django.urls import reverse

from .bot_logic import get_bot_response
from .forms import LeadForm
from .models import Lead


class LeadModelAndFormTests(TestCase):
    def test_valid_lead_is_saved(self):
        lead = Lead.objects.create(
            name="John Miller",
            email="john@example.com",
            phone="3125551122",
            requirement="Custom sectional sofa",
            message="I need a grey sectional sofa for my living room.",
            preferred_contact_time="Evening",
        )

        self.assertEqual(Lead.objects.count(), 1)
        self.assertEqual(lead.name, "John Miller")
        self.assertEqual(lead.status, "New")
        self.assertEqual(lead.source, "Website AI Bot")

    def test_lead_requires_name(self):
        form = LeadForm(data={
            "name": "",
            "email": "test@example.com",
            "phone": "",
            "requirement": "Custom bed",
            "message": "I need a king-size custom bed.",
            "preferred_contact_time": "",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_lead_requires_contact(self):
        form = LeadForm(data={
            "name": "Sarah Wilson",
            "email": "",
            "phone": "",
            "requirement": "Custom dining table",
            "message": "I need a 6-seater dining table.",
            "preferred_contact_time": "",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)

    def test_lead_requires_requirement(self):
        form = LeadForm(data={
            "name": "Michael Brown",
            "email": "",
            "phone": "3125554444",
            "requirement": "",
            "message": "I need furniture for my apartment.",
            "preferred_contact_time": "",
        })

        self.assertFalse(form.is_valid())
        self.assertIn("requirement", form.errors)


class BotLogicTests(TestCase):
    def test_faq_question_returns_answer(self):
        response = get_bot_response("Do you make custom furniture?")

        self.assertIn("UrbanNest makes custom furniture", response)

    def test_unknown_question_returns_fallback(self):
        response = get_bot_response("Do you sell mobile phones?")

        self.assertIn("UrbanNest focuses on furniture", response)


class PageAndRouteTests(TestCase):
    def test_leads_page_loads(self):
        Lead.objects.create(
            name="John Miller",
            email="john@example.com",
            phone="3125551122",
            requirement="Custom sectional sofa",
            message="I need a grey sectional sofa.",
        )

        response = self.client.get(reverse("lead_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "UrbanNest Lead List")
        self.assertContains(response, "John Miller")