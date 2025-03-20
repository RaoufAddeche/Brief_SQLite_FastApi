# Connexion à SQLite et création des tables
import sqlite3
from app.config import DATABASE_URL
# Connexion à la base de données SQLite
def get_connection():
    conn = sqlite3.connect(DATABASE_URL)
    conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par leur nom
    return conn

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    #Table des utilisateurs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        pseudo TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        is_coach NUMERIC NOT NULL);
        
    """)


    #Table des caractéristiques
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS caracteristic (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            gender TEXT NOT NULL,
            age INTEGER NOT NULL,
            weight REAL NOT NULL,
            height REAL NOT NULL,
            id_user INTEGER,
            FOREIGN KEY(id_user) REFERENCES user(id));
    """)

    #Table des perfomances
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS performance (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            power_max REAL,
            hr_max REAL,
            vo2_max real,
            rf_max REAL,
            cadence_max REAL,
            date DATE DEFAULT (DATE('now')),
            athlete_id INTEGER NOT NULL,
            test_type_id INTEGER NOT NULL,
            FOREIGN KEY (athlete_id) REFERENCES user (id),
            FOREIGN KEY(test_type_id) REFERENCES test_type(id));
    """)

    #Table des types_tests
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_type (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name_type TEXT NOT NULL);
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()

