from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, users, events

app = FastAPI(
    title="MUSE API",
    description="Consumer Intelligence Platform API",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configurar em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix="/api/v1/health", tags=["health"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(events.router, prefix="/api/v1/events", tags=["events"])

@app.get("/")
async def root():
    return {
        "name": "MUSE",
        "description": "Consumer Intelligence Platform",
        "status": "operational"
    }
