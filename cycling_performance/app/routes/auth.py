# Routes for authentication
from fastapi import APIRouter, HTTPException
from app.db.queries import add_user, get_user_by_email
from app.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES
from app.utils.security import hash_password, verify_password, create_access_token
from datetime import timedelta
from app.schema.user import UserConnexion, LoginUser
from app.db.database import get_connection

router = APIRouter()

@router.post("/register")
def register_user(user: UserConnexion):
    """
    Register a new user in the database.
    """
    # Hash the user's password
    hashed_password = hash_password(user.password)
    try:
        # Add the user to the database
        add_user(user.pseudo, user.email, hashed_password, user.is_coach)
        return {"message": "User successfully registered"}
    except Exception as e:
        # Raise an exception if registration fails
        raise HTTPException(status_code=400, detail="Error during registration")


@router.post("/login")
def login_user(user: LoginUser):
    """
    Authenticate a user and generate a JWT token.
    """
    print(user.email)
    # Retrieve the user from the database by email
    db_user = get_user_by_email(user.email)
    # Verify the user's password
    if not user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect email or password")

    # Generate a JWT token
    acces_token = create_access_token(
        data={"sub": db_user["email"]}, expires_delta=timedelta(minutes=30)
    )
    return {"acces_token": acces_token, "token_type": "bearer"}


@router.delete("/account/{user_id}")
def delete_user(user_id: int):
    """
    Delete a user and all associated data.
    """
    # Get a connection to the database
    conn = get_connection()
    cursor = conn.cursor()

    # Check if the user exists
    cursor.execute("SELECT * FROM user WHERE id = ?;", (user_id,))
    user = cursor.fetchone()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Delete associated performance records
    cursor.execute("DELETE FROM performance WHERE athlete_id = ?;", (user_id,))

    # Delete associated characteristics
    cursor.execute("DELETE FROM caracteristic WHERE id_user = ?;", (user_id,))

    # Delete the user
    cursor.execute("DELETE FROM user WHERE id = ?;", (user_id,))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return {"message": "User and associated data successfully deleted"}