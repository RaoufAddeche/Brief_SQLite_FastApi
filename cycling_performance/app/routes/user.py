from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserLogin, UserRead, UserUpdate, UserUpdatePassword

import sqlite3

router = APIRouter()


@router.get("/users/{id}")
async def read_user(id: int):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    SELECT id, pseudo, email, password, is_coach FROM user
    WHERE id = ?;
    """

    cursor.execute(request, (id,))
    result = cursor.fetchall() # Récupération de tous les résultats dans une liste
    print(result)
    conn.close()
    return result


@router.get("/users")
async def read_user_all():
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    SELECT id, pseudo, email, password, is_coach FROM user;
    """

    cursor.execute(request)
    results = cursor.fetchall() # Récupération de tous les résultats dans une liste

    print(results) # Affichage des résultats
    conn.close() # Fermeture de la connexion
    return results


@router.post("/users/add", response_model=UserCreate)
async def create_user(create_user: UserCreate):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    pseudo = create_user.pseudo
    email = create_user.email
    password = create_user.password
    is_coach = create_user.is_coach

    print(f"pseudo = {pseudo}, email = {email}, password = {password}, is_coach = {str(is_coach)}")

    request = """
    INSERT INTO user (pseudo, email, password, is_coach)
    VALUES (?, ?, ?, ?);"""

    cursor.execute(request, (pseudo, email, password, is_coach))
    conn.commit()
    conn.close()


@router.patch("/users/update/{id_user}", response_model=UserUpdate)
async def update_user(id_user: int, update_user: UserUpdate):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    UPDATE user 
    SET pseudo = ?, email = ? 
    WHERE id = ?;
    """

    cursor.execute(request, (pseudo, email, id))
    conn.commit()
    conn.close()


@router.patch("/users/update_password/{id_user}", response_model=UserUpdatePassword)
async def update_user_password(id_user: int, password_updated: UserUpdatePassword):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    password = password_updated.password

    request = """
    UPDATE user 
    SET password = ?
    WHERE id = ?;
    """

    cursor.execute(request, (password, id_user))
    conn.commit()
    conn.close()


@router.delete("/users/{id_user}")
async def delete_user(id_user):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    DELETE FROM user 
    WHERE id = ?;
    """

    cursor.execute(request, (id_user,))
    conn.commit()
    conn.close()
