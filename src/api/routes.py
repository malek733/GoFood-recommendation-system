from fastapi import APIRouter
from src.models.recommender import recommend_for_user
from src.agents.manager_agent import manager_agent

router = APIRouter()

@router.get("/recommend/{user_id}")
def recommend(user_id: str):
    recs = recommend_for_user(user_id, [], [])
    return {"user_id": user_id, "recommendations": recs}

@router.post("/manager-order")
def manager_order(data: dict):
    state = {"manager_input": data.get("message")}
    result = manager_agent.invoke(state)
    return {"response": result["intent"]}
