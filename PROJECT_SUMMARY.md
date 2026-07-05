# Project Summary — UrbanNest Website AI Support Bot + Lead Capture

## Project Name

UrbanNest Website AI Support Bot + Lead Capture

## Purpose

This project is a portfolio/MVP web app for a mock furniture business. It helps website visitors ask basic furniture questions and submit quote requests.

## Mock Client

UrbanNest Furniture Studio  
Location: Chicago, Illinois, USA  
Business Type: Furniture store and custom furniture provider

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- JavaScript

## Main Features Completed

- Customer-facing chatbot page
- AI-style rule-based chatbot responses
- Furniture FAQ answering
- Product and pricing guidance
- Delivery answer
- Quote/contact intent response
- Safe fallback for outside-scope questions
- Lead capture form
- Lead validation
- Lead storage in SQLite database
- Portfolio/MVP owner lead list page
- Clean UI styling
- Automated tests

## Main Pages

- `/` — Chatbot homepage
- `/chat/` — Chatbot response endpoint
- `/submit-lead/` — Lead form submission endpoint
- `/leads/` — Portfolio/MVP owner lead list page
- `/admin/` — Django admin, optional

## Tests Completed

Automated tests completed:

- Valid lead saves successfully
- Lead requires name
- Lead requires email or phone
- Lead requires requirement
- FAQ question returns correct answer
- Outside-scope question returns fallback
- Lead list page loads correctly

Manual tests completed:

- FAQ question
- Sofa pricing question
- Chicago delivery question
- Quote intent question
- Mobile phone fallback question
- Missing contact validation
- Missing name validation
- Missing requirement validation
- Valid lead submission
- Lead list display

## Known Limitations

- This is a portfolio/MVP project.
- Bot uses rule-based logic, not OpenAI API.
- Lead page is a simple portfolio/MVP lead view.
- Real client version should use a secure dashboard/admin portal.
- No CRM integration.
- No WhatsApp integration.
- No payment system.
- No analytics dashboard.
- No email notifications.

## Future Upgrade Ideas

- Secure owner dashboard
- Login-protected lead management
- Email notification for new leads
- CRM integration
- WhatsApp Business API integration
- OpenAI API or RAG-based chatbot
- Chat history dashboard
- Analytics dashboard
- Appointment booking
- Product catalog search

## Portfolio Use

This project can be shown as a client-style portfolio project for small businesses that need website support automation and lead capture.