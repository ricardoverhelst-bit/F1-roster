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


def main():
    create_tables()
    add_team()


if __name__ == "__main__":
    main()
