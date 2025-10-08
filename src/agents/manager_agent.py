from langgraph.graph import StateGraph
from langchain_groq import ChatGroq
from src.config.supabase_client import supabase

model = ChatGroq(model="llama-3.1-8b-instant")

def recognize_intent(state):
    query = state["manager_input"]
    response = model.invoke(f"Extract food intent: {query}")
    state["intent"] = response.content
    return state

def create_order(state):
    items = state["intent"]
    supabase.table("orders").insert({
        "manager_initiated": True,
        "items": items
    }).execute()
    return state

graph = StateGraph()
graph.add_node("recognize_intent", recognize_intent)
graph.add_node("create_order", create_order)
graph.add_edge("recognize_intent", "create_order")
graph.set_entry_point("recognize_intent")
manager_agent = graph.compile()
