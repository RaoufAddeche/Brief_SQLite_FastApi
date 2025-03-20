# Requêtes SQL pour les opérations CRUD

from app.db.database import get_connection


# Ajouter un utilisateur
def add_user(pseudo, email, password, is_coach):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user (pseudo, email, password, is_coach) VALUES (?, ?, ?, ?);",
        (pseudo, email, password, is_coach)
    )
    conn.commit()
    conn.close()

#Récuperer l'utilisateur par email
def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email= ?;", (email))
    user= cursor.fetchone()
    conn.close()
    return user

# Récuperer un utilisateur par email
def add_caracteristic(gender, age, weight, height, id_user):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO caracteristic (gender, age ,weight, height, id_user) VALUES (?, ?, ?, ?, ?);",
        (gender, age, weight, height, id_user)
    )
    conn.commit()
    conn.close()

#Ajouter un type de test
def add_test_type(name_type):
    conn= get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO test_type (name_type) VALUES (?);",
        (name_type)
    )
    conn.commit()
    conn.close()

#Ajouter un test
def add_test(power_max, hr_max, vo2_max, rf_max, cadence_max, athlete_id, test_type_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO test (power_max, hr_max, vo2_max, rf_max, cadence_max, athlete_id, test_type_id)
        VALUES (?, ?, ?, ?, ?, ?, ?);""",
        (power_max, hr_max, vo2_max, rf_max, cadence_max, athlete_id, test_type_id)
    )
    conn.commit()
    conn.close()

# Récupérer les tests d'un athlète
def get_tests_by_athlete(athlete_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test WHERE athlete_id = ?;", (athlete_id,))
    tests = cursor.fetchall()
    conn.close()
    return tests

# Récupérer les types de tests
def get_test_types():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_type;")
    test_types = cursor.fetchall()
    conn.close()
    return test_types