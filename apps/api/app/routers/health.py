from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.database import get_db

router = APIRouter()

@router.get("/")
async def health_check():
    return {"status": "healthy", "service": "muse-api"}

@router.get("/database")
async def database_health(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": str(e)}
