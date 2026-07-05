# UrbanNest Website AI Support Bot + Lead Capture — Case Study

## Problem

UrbanNest Furniture Studio receives repeated website questions about furniture options, custom orders, pricing, delivery, materials, and quote requests.

Many interested visitors may leave the website without submitting a contact form, causing missed leads.

## Solution

A website AI-style support bot was built for UrbanNest Furniture Studio.

The bot answers common customer questions using approved business information and guides interested visitors toward submitting a quote request.

When a visitor wants pricing, contact, or a custom furniture quote, the system provides clear guidance and allows the visitor to submit lead details through a quote form.

## Key Features

- Customer-facing chatbot page
- Rule-based AI-style response logic
- FAQ and product/service answering
- Starting price guidance in USD
- Delivery and business policy answers
- Quote/contact intent response
- Lead capture form
- Lead validation
- Lead storage in SQLite database
- Portfolio/MVP owner lead list page
- Safe fallback for unrelated questions
- Automated tests for core workflows

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript

## Testing Completed

Manual testing included:

- FAQ questions
- Product/pricing questions
- Delivery questions
- Quote/contact intent
- Lead form submission
- Missing contact validation
- Missing name validation
- Missing requirement validation
- Outside-scope fallback
- Owner lead list page

Automated tests included:

- Valid lead saving
- Missing name validation
- Missing contact validation
- Missing requirement validation
- FAQ response
- Fallback response
- Lead list page loading

## Result

The project shows how a small business website can use a simple AI-style support bot to answer repeated questions and collect customer inquiries.

This helps reduce manual support work and improves lead capture from interested website visitors.

## Limitations

This is a portfolio/MVP version.

Current limitations:

- No OpenAI API integration
- No CRM integration
- No WhatsApp integration
- No email notifications
- No advanced analytics dashboard
- No secure owner dashboard yet
- No payment or order tracking
- Rule-based bot logic only

## Future Upgrades

Possible upgrades include:

- Secure owner dashboard
- Login-protected lead management
- Email notification for new leads
- CRM integration
- WhatsApp Business API integration
- Chat history dashboard
- Analytics dashboard
- OpenAI API or RAG-based answering
- Appointment booking
- Product catalog search