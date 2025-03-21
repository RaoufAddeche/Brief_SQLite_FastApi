# Main entry point for the FastAPI application
from fastapi import FastAPI
from app.db.database import create_tables
from app.routes import auth, athlete, stats, performance

# Initialize the FastAPI application
app = FastAPI()

# Include the authentication routes
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

# Include the athlete management routes
app.include_router(athlete.router, prefix="/athletes", tags=["Athletes"])

# Include the performance management routes
app.include_router(performance.router, prefix="/performances", tags=["Performances"])

# Include the statistics routes
app.include_router(stats.router, prefix="/stats", tags=["Statistics"])

# Create database tables on application startup
@app.on_event("startup")
def startup_event():
    """
    Event triggered when the application starts.
    Ensures that all required database tables are created.
    """
    create_tables()