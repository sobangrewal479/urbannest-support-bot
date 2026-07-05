def get_bot_response(user_message):
    message = user_message.lower().strip()

    if not message:
        return "Please type a question so I can help you."

    outside_scope_keywords = [
        "mobile phone",
        "mobile phones",
        "phone",
        "phones",
        "flight",
        "weather",
        "bank loan",
        "university assignment",
        "kitchen appliance",
        "gold",
        "cryptocurrency",
        "refrigerator",
        "fridge",
    ]

    if any(keyword in message for keyword in outside_scope_keywords):
        return (
            "Sorry, I don’t have exact information about that. UrbanNest focuses on furniture "
            "such as sofas, beds, wardrobes, dining tables, office furniture, TV consoles, "
            "coffee tables, and custom furniture. If you need furniture help, please share "
            "your details in the quote form."
        )

    if "do you make custom furniture" in message or "make custom furniture" in message:
        return (
            "Yes, UrbanNest makes custom furniture including sofas, beds, wardrobes, "
            "dining tables, TV consoles, office desks, and storage units. Final pricing "
            "depends on size, material, fabric, finish, and design."
        )

    if message in ["price", "cost", "what is the price", "what is the cost"]:
        return (
            "Which furniture item are you interested in? For example: sofa, bed, "
            "dining table, wardrobe, or office desk."
        )

    lead_keywords = [
        "i want to buy",
        "need a quote",
        "request a quote",
        "can someone contact",
        "call me",
        "contact me",
        "place an order",
        "want to order",
        "what will it cost",
        "exact price",
        "exact quote",
        "whatsapp",
        "consultation",
        "i need furniture",
        "i need a custom",
        "i want a custom",
    ]

    if any(keyword in message for keyword in lead_keywords):
        return (
            "Sure, I can help with that. For an exact quote, please share your name, "
            "phone or email, requirement, and message using the quote form."
        )

    if "sofa" in message or "sectional" in message:
        return (
            "UrbanNest offers 2-seater, 3-seater, sectional, and custom sofa sets. "
            "Sofas usually start from $899. Final pricing depends on size, fabric, "
            "foam quality, frame material, and design."
        )

    if "bed" in message:
        return (
            "UrbanNest offers twin, queen, king, and upholstered beds. Beds usually "
            "start from $699. Custom sizes and finishes are available."
        )

    if "dining" in message or "table" in message:
        return (
            "UrbanNest offers 4-seater, 6-seater, and 8-seater dining table sets. "
            "Dining tables usually start from $1,099. Custom designs are available."
        )

    if "wardrobe" in message or "closet" in message:
        return (
            "UrbanNest offers sliding, hinged, and custom-size wardrobes or closet "
            "storage units. These usually start from $1,499."
        )

    if "office" in message or "desk" in message:
        return (
            "UrbanNest offers home office desks, executive desks, and workstations. "
            "Office desks usually start from $499."
        )

    if "tv console" in message or "console" in message:
        return (
            "UrbanNest offers wall-mounted and floor-standing TV consoles. "
            "TV consoles usually start from $599."
        )

    if "coffee table" in message:
        return (
            "UrbanNest offers wooden, marble-top, and modern coffee tables. "
            "Coffee tables usually start from $249."
        )

    if "custom furniture" in message or "custom" in message:
        return (
            "Yes, UrbanNest makes custom furniture including sofas, beds, wardrobes, "
            "dining tables, TV consoles, office desks, and storage units. Final pricing "
            "depends on size, material, fabric, finish, and design."
        )

    if "deliver" in message or "delivery" in message:
        return (
            "UrbanNest delivers in Chicago, nearby suburbs, and selected Illinois areas. "
            "Delivery charges depend on area, item size, and order value."
        )

    if "material" in message or "wood" in message or "fabric" in message:
        return (
            "UrbanNest uses solid wood, engineered wood, MDF, plywood, premium fabric, "
            "leatherette, foam, metal frames for selected office furniture, and polish "
            "or paint finishes. Exact material depends on budget, design, and durability needs."
        )

    if "time" in message or "timing" in message or "hours" in message or "open" in message:
        return (
            "UrbanNest is open Monday to Saturday from 10:00 AM to 7:00 PM. "
            "Sunday visits are by appointment only."
        )

    if "warranty" in message:
        return (
            "UrbanNest offers warranty on selected furniture items. Warranty details "
            "depend on product type, material, and usage conditions."
        )

    if "showroom" in message or "location" in message or "address" in message:
        return (
            "UrbanNest Furniture Studio is based in Chicago, Illinois, USA. "
            "Customers can contact the team for showroom visit details or quote requests."
        )

    if "what furniture" in message or "products" in message or "what do you sell" in message:
        return (
            "UrbanNest offers sofas, beds, dining tables, wardrobes, office desks, "
            "TV consoles, coffee tables, and custom furniture."
        )

    return (
        "Sorry, I don’t have exact information about that. UrbanNest focuses on furniture "
        "such as sofas, beds, wardrobes, dining tables, office furniture, TV consoles, "
        "coffee tables, and custom furniture. If you need furniture help, please share "
        "your details in the quote form."
    )