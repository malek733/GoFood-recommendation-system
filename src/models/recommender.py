def recommend_for_user(user_id, orders, menu):
    # Simple placeholder logic
    history = [o for o in orders if o["user_id"] == user_id]
    return menu[:3]
