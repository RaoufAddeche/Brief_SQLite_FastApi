# Point d'entrée principal de l'application FastAPI
from fastapi import FastAPI
from app.db.database import create_tables
from app.routes import auth, athlete, stats, performance
#Initialisation de l'app FastAPI

app= FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["Authentification"])
app.include_router(athlete.router, prefix="/athletes", tags=["Athletes"])
app.include_router(performance.router, prefix="/performances", tags=["Performances"])
app.include_router(stats.router, prefix="/stats", tags=["Statistics"])

#Création des tables au démarrage
@app.on_event("startup")
def startup_event():
    create_tables()