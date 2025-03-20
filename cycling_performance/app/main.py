# Point d'entrée principal de l'application FastAPI
from fastapi import FastAPI
from app.db.database import create_tables
from app.routes import auth, athlete, test, stats

#Initialisation de l'app FastAPI

app= FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["Authentification"])
app.include_router(athlete.router, prefix="/athletes", tags=["Athletes"])
app.include_router(test.router, prefix="/tests", tags=["Tests"])
app.include_router(stats.router, prefix="/stats", tags=["Statistics"])

#Création des tables au démarrage
@app.on_event("startup"):
    create_tables()