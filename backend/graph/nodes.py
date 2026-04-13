from llm.groq_client import get_llm

llm = get_llm()


# ── INTENT DETECTION ──
def detect_intent(state):
    user_input = state.get("user_input", "").lower()

    if "recommend" in user_input or "suggest" in user_input:
        intent = "recommend"
    elif "order" in user_input or "delivery" in user_input:
        intent = "order"
    elif "return" in user_input or "refund" in user_input:
        intent = "return"
    else:
        intent = "general"

    return {
        "user_input": user_input,
        "intent": intent,
        "response": state.get("response", "")
    }


# ── ROUTER ──
def route_intent(state):
    intent = state.get("intent", "general")

    if intent == "recommend":
        return "product"
    elif intent in ["order", "return"]:
        return "faq"
    else:
        return "casual"


# ── PRODUCT NODE ──
def product_node(state):
    return {
        "user_input": state.get("user_input", ""),
        "intent": state.get("intent", ""),
        "response": "🔥 I recommend: Dior Sauvage, Bleu de Chanel, YSL Y"
    }


# ── FAQ NODE ──
def faq_node(state):
    return {
        "user_input": state.get("user_input", ""),
        "intent": state.get("intent", ""),
        "response": "📦 Orders: Track in profile | 🔁 Returns: within 7 days"
    }


# ── CASUAL CHAT (LLM) ──
def casual_node(state):
    user_input = state.get("user_input", "")

    reply = llm.invoke(user_input)

    # fix AIMessage
    if hasattr(reply, "content"):
        reply = reply.content

    return {
        "user_input": user_input,
        "intent": state.get("intent", ""),
        "response": reply
    }