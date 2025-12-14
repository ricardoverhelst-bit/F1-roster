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

def menu():
    print("F1 TEAM ROSTER")
    print("1. Team toevoegen")
    print("2. Driver toevoegen")
    print("0. Afsluiten")

    return input("Maak een keuze: ")

def main():
    create_tables()

    while True:
        choice = menu()

        if choice == "1":
            add_team()
        elif choice == "2":
            add_driver()
        elif choice == "0":
            print("Programma afgesloten")
            break
        else:
            print("Ongeldige keuze\n")


if __name__ == "__main__":
    main()
