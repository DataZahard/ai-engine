def generate_product_metadata(name, description):
    # Simulates AI logic without needing an API key
    return {
        "primary_category": "Eco-Friendly Goods",
        "sub_category": "Sustainable Living",
        "tags": ["reusable", "organic"],
        "sustainability_score": 5
    }

def handle_whatsapp_logic(user_id, message):
    # Simulates escalation logic (Escalates if 'refund' is in message)
    should_escalate = "refund" in message.lower()
    return {
        "reply": "Thank you for reaching out. We are processing your request.",
        "escalate": should_escalate
    }

