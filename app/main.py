from app.database import create_tables, get_connection
import csv

# =========================
# TEAM TOEVOEGEN
# =========================
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


# =========================
# DRIVER TOEVOEGEN
# =========================
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


# =========================
# CSV EXPORT
# =========================
def export_teams_csv():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM teams")
    teams = cursor.fetchall()

    conn.close()

    with open("teams.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "country"])
        writer.writerows(teams)

    print("teams.csv aangemaakt\n")

def export_drivers_csv():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM drivers")
    drivers = cursor.fetchall()

    conn.close()

    with open("drivers.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "number", "team_id"])
        writer.writerows(drivers)

    print("drivers.csv aangemaakt\n")


# =========================
# MENU
# =========================
def menu():
    print("F1 TEAM ROSTER")
    print("1. Team toevoegen")
    print("2. Driver toevoegen")
    print("3. Exporteer teams naar CSV")
    print("4. Exporteer drivers naar CSV")
    print("0. Afsluiten")

    return input("Maak een keuze: ")


# =========================
# MAIN
# =========================
def main():
    create_tables()

    while True:
        choice = menu()

        if choice == "1":
            add_team()
        elif choice == "2":
            add_driver()
        elif choice == "3":
            export_teams_csv()
        elif choice == "4":
            export_drivers_csv()
        elif choice == "0":
            print("Programma afgesloten")
            break
        else:
            print("Ongeldige keuze\n")


if __name__ == "__main__":
    main()
