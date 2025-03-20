from faker import Faker
import random
from app.db.database import get_connection

fake = Faker()

def generate_test_types():
    """
    Génère des types de tests fictifs dans la table `test_type`.
    """
    conn = get_connection()
    cursor = conn.cursor()

    test_types = [
        "Test de puissance maximale",
        "Test d'endurance",
        "Test de VO2max",
        "Test de sprint",
        "Test de récupération"
    ]

    for test_type in test_types:
        cursor.execute(
            """
            INSERT INTO test_type (name_type)
            VALUES (?);
            """,
            (test_type,),
        )

    conn.commit()
    conn.close()
    print(f"{len(test_types)} types de tests ont été ajoutés à la base de données.")

def generate_fake_cyclists_and_performances(num_cyclists=200):
    """
    Génère des cyclistes fictifs, leurs caractéristiques et leurs performances.
    """
    conn = get_connection()
    cursor = conn.cursor()

    # Ensemble pour stocker les emails uniques
    used_emails = set()

    for _ in range(num_cyclists):
        # Générer un email unique
        email = fake.email()
        while email in used_emails:  # Vérifier si l'email est déjà utilisé
            email = fake.email()
        used_emails.add(email)

        # Générer un utilisateur (cycliste)
        pseudo = fake.user_name()
        password = fake.password()
        is_coach = random.choice([0, 1])  # 0 = athlète, 1 = coach

        # Insérer l'utilisateur dans la table `user`
        cursor.execute(
            """
            INSERT INTO user (pseudo, email, password, is_coach)
            VALUES (?, ?, ?, ?);
            """,
            (pseudo, email, password, is_coach),
        )
        user_id = cursor.lastrowid  # Récupérer l'ID de l'utilisateur inséré

        # Générer des caractéristiques pour l'utilisateur
        gender = random.choice(["M", "F"])
        age = random.randint(18, 40)
        weight = round(random.uniform(50, 90), 1)  # Poids entre 50 et 90 kg
        height = round(random.uniform(1.5, 2.0), 2)  # Taille entre 1.5m et 2.0m

        # Insérer les caractéristiques dans la table `caracteristic`
        cursor.execute(
            """
            INSERT INTO caracteristic (gender, age, weight, height, id_user)
            VALUES (?, ?, ?, ?, ?);
            """,
            (gender, age, weight, height, user_id),
        )

        # Générer des performances pour l'utilisateur
        for _ in range(random.randint(1, 5)):  # Chaque utilisateur a entre 1 et 5 performances
            power_max = round(random.uniform(200, 500), 1)  # Puissance max entre 200 et 500 W
            hr_max = random.randint(150, 200)  # Fréquence cardiaque max entre 150 et 200 bpm
            vo2_max = round(random.uniform(40, 70), 1)  # VO2max entre 40 et 70 ml/kg/min
            rf_max = random.randint(30, 50)  # RF max entre 30 et 50
            cadence_max = random.randint(80, 120)  # Cadence max entre 80 et 120 rpm
            test_type_id = random.randint(1, 5)  # ID du type de test (1 à 5)

            # Insérer la performance dans la table `performance`
            cursor.execute(
                """
                INSERT INTO performance (power_max, hr_max, vo2_max, rf_max, cadence_max, athlete_id, test_type_id)
                VALUES (?, ?, ?, ?, ?, ?, ?);
                """,
                (power_max, hr_max, vo2_max, rf_max, cadence_max, user_id, test_type_id),
            )

    conn.commit()
    conn.close()
    print(f"{num_cyclists} cyclistes fictifs et leurs performances ont été ajoutés à la base de données.")

if __name__ == "__main__":
    # Générer les types de tests
    generate_test_types()

    # Générer les cyclistes et leurs performances
    generate_fake_cyclists_and_performances(200)
    # python -m app.faker.generate_cyclists 