from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime

router = APIRouter()

class EventCreate(BaseModel):
    user_id: int
    event_type: str
    data: Dict[str, Any] = {}
    timestamp: datetime = datetime.now()

class EventResponse(BaseModel):
    id: int
    user_id: int
    event_type: str
    data: Dict[str, Any]
    timestamp: datetime

# Event types
EVENT_TYPES = [
    "USER_LIKED_POST",
    "USER_SAVED_LOOK",
    "USER_REJECTED_LOOK",
    "USER_VIEWED_PRODUCT",
    "USER_SEARCHED_STYLE",
    "USER_ADDED_CLOTHING",
    "USER_WORE_OUTFIT",
    "USER_COMPLETED_QUIZ",
    "USER_DISCOVERED_STYLE",
    "USER_FOLLOWED_CREATOR",
    "USER_VIEWED_TREND",
    "USER_PURCHASED_PRODUCT"
]

@router.post("/", response_model=EventResponse)
async def create_event(event: EventCreate):
    if event.event_type not in EVENT_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid event type. Must be one of: {', '.join(EVENT_TYPES)}"
        )
    # Implementação futura
    return {"message": "Event creation endpoint"}

@router.get("/user/{user_id}")
async def get_user_events(user_id: int):
    # Implementação futura
    return {"message": f"Get events for user {user_id}"}

@router.get("/types")
async def get_event_types():
    return {"event_types": EVENT_TYPES}
