
from fastapi import FastAPI
from app.database import Base, engine

# Import models
from app.models import user, record

# Import routes
from app.routes import user_routes, record_routes, dashboard_routes

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)


@app.get("/")
def home():
    return {"message": "Finance Backend Running"}
