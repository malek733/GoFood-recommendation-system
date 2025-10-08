from src.config.supabase_client import supabase

def get_orders():
    return supabase.table("orders").select("*").execute().data

def get_menu():
    return supabase.table("menu_items").select("*").execute().data
