import sqlite3


def create_user(pseudo, email, password):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    INSERT INTO user (pseudo, email, password, is_coach)
    VALUES (?, ?, ?, 0);"""

    cursor.execute(request, (pseudo, email, password))
    conn.commit()
    conn.close()


def show_user(id):
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


def show_all_users():
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    SELECT pseudo, email, password, is_coach FROM user;
    """

    cursor.execute(request)
    result = cursor.fetchall() # Récupération de tous les résultats dans une liste
    print(result)
    conn.close()


def update_user(id, pseudo, email):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    UPDATE user 
    SET pseudo = ?, email = ? 
    WHERE id = ?;
    """

    cursor.execute(request, (pseudo, email, id))
    result = cursor.fetchall()
    print(result)
    conn.close()

def delete_user(id):
    conn = sqlite3.connect('database.db') # Connexion à la base de données
    cursor = conn.cursor() # Création d'un curseur

    request = """
    DELETE FROM user 
    WHERE id = ?;
    """

    cursor.execute(request, (id,))
    result = cursor.fetchall()
    print(result)
    conn.close()