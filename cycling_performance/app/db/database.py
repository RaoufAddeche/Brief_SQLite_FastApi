# SQLite connection and table creation
import sqlite3
from app.config import DATABASE_URL

# Connect to the SQLite database
def get_connection():
    """
    Establish a connection to the SQLite database.
    Returns a connection object with row access by column names.
    """
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # Allows access to columns by their names
    return conn

# Create the necessary tables in the database
def create_tables():
    """
    Create all required tables in the SQLite database if they do not already exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # User table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        pseudo TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        is_coach NUMERIC NOT NULL
    );
    """)

    # Characteristics table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS caracteristic (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        gender TEXT NOT NULL,
        age INTEGER NOT NULL,
        weight REAL NOT NULL,
        height REAL NOT NULL,
        id_user INTEGER,
        FOREIGN KEY(id_user) REFERENCES user(id)
    );
    """)

    # Performance table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS performance (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        power_max REAL,
        hr_max REAL,
        vo2_max REAL,
        rf_max REAL,
        cadence_max REAL,
        date DATE DEFAULT (DATE('now')),
        athlete_id INTEGER NOT NULL,
        test_type_id INTEGER NOT NULL,
        FOREIGN KEY (athlete_id) REFERENCES user (id),
        FOREIGN KEY(test_type_id) REFERENCES test_type(id)
    );
    """)

    # Test types table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS test_type (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name_type TEXT NOT NULL
    );
    """)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Run the table creation script if executed directly
if __name__ == "__main__":
    create_tables()