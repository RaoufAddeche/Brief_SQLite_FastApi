# SQL queries for CRUD operations

from app.db.database import get_connection

# Add a new user to the database
def add_user(pseudo, email, password, is_coach):
    """
    Insert a new user into the 'user' table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user (pseudo, email, password, is_coach) VALUES (?, ?, ?, ?);",
        (pseudo, email, password, is_coach)
    )
    conn.commit()
    conn.close()

# Retrieve a user by email
def get_user_by_email(email):
    """
    Fetch a user from the 'user' table using their email.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ?;", (email,))
    user = cursor.fetchone()
    conn.close()
    return user

# Add characteristics for a user
def add_caracteristic(gender, age, weight, height, id_user):
    """
    Insert a new characteristic into the 'caracteristic' table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO caracteristic (gender, age, weight, height, id_user) VALUES (?, ?, ?, ?, ?);",
        (gender, age, weight, height, id_user)
    )
    conn.commit()
    conn.close()

# Add a new test type
def add_test_type(name_type):
    """
    Insert a new test type into the 'test_type' table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO test_type (name_type) VALUES (?);",
        (name_type,)
    )
    conn.commit()
    conn.close()

# Add a new performance
def add_performance(power_max, hr_max, vo2_max, rf_max, cadence_max, athlete_id, test_type_id):
    """
    Insert a new performance into the 'performance' table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO performance (power_max, hr_max, vo2_max, rf_max, cadence_max, athlete_id, test_type_id)
        VALUES (?, ?, ?, ?, ?, ?, ?);""",
        (power_max, hr_max, vo2_max, rf_max, cadence_max, athlete_id, test_type_id)
    )
    conn.commit()
    conn.close()

# Retrieve all performances for a specific athlete
def get_performances_by_athlete(athlete_id):
    """
    Fetch all performances for a given athlete from the 'performance' table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM performance WHERE athlete_id = ?;", (athlete_id,))
    performances = cursor.fetchall()
    conn.close()
    return performances

# Retrieve all test types
def get_test_types():
    """
    Fetch all test types from the 'test_type' table.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test_type;")
    test_types = cursor.fetchall()
    conn.close()
    return test_types