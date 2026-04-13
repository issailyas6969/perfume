def route(state):
    intent = state["intent"]

    if "product" in intent:
        return "product"
    elif "faq" in intent:
        return "faq"
    else:
        return "casual"