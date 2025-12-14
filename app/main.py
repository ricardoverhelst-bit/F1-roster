from app.database import create_tables, get_connection

def add_team():
    print("\n--- TEAM TOEVOEGEN ---")

    name = input("Teamnaam: ")
    country = input("Land: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO teams (name, country) VALUES (?, ?)",
        (name, country)
    )

    conn.commit()
    conn.close()

    print("Team toegevoegd\n")

def add_driver():
    print("\n--- DRIVER TOEVOEGEN ---")

    name = input("Naam rijder: ")
    number = input("Rugnummer: ")
    team_id = input("Team ID: ")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO drivers (name, number, team_id) VALUES (?, ?, ?)",
        (name, number, team_id)
    )

    conn.commit()
    conn.close()

    print("Driver toegevoegd\n")

def main():
    create_tables()
    add_driver()


if __name__ == "__main__":
    main()
