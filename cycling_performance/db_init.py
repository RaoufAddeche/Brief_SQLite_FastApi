import sqlite3

# Create tables
def create_user_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    request = """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        pseudo TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        is_coach NUMERIC NOT NULL
    )
    """
    cursor.execute(request)
    conn.commit()
    conn.close()


def create_caracteristic_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    request = """
    CREATE TABLE IF NOT EXISTS caracteristic (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        gender TEXT NOT NULL,
        age INTEGER,
        weight REAL,
        height REAL,
        id_user INTEGER,
        FOREIGN KEY(id_user) REFERENCES user(id)
    )"""
    cursor.execute(request)
    conn.commit()
    conn.close()


def create_test_type_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    request = """
    CREATE TABLE IF NOT EXISTS test_type (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name_type TEXT NOT NULL
    )"""
    cursor.execute(request)
    conn.commit()
    conn.close()


def create_test_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    request = """
    CREATE TABLE IF NOT EXISTS test (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        power_max REAL,
        hr_max REAL,
        vo2_max REAL,
        rf_max REAL,
        cadence_max REAL,
        date DATE DEFAULT (DATE('now')),
        id_user INTEGER,
        id_test_type INTEGER,
        FOREIGN KEY(id_user) REFERENCES user(id),
        FOREIGN KEY(id_test_type) REFERENCES test_type(id)
    )"""
    cursor.execute(request)
    conn.commit()
    conn.close()


# Create tables
def create_tables():
    create_user_table()
    create_caracteristic_table()
    create_test_type_table()
    create_test_table()

# create_tables()