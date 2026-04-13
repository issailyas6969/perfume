from langgraph.graph import StateGraph
from graph.nodes import (
    detect_intent,
    product_node,
    faq_node,
    casual_node,
    route_intent
)

def build_graph():
    builder = StateGraph(dict)

    # nodes
    builder.add_node("intent", detect_intent)
    builder.add_node("product", product_node)
    builder.add_node("faq", faq_node)
    builder.add_node("casual", casual_node)

    builder.set_entry_point("intent")

    builder.add_conditional_edges(
        "intent",
        route_intent,
        {
            "product": "product",
            "faq": "faq",
            "casual": "casual"
            }
    )

    builder.set_finish_point("product")
    builder.set_finish_point("faq")
    builder.set_finish_point("casual")

    return builder.compile()