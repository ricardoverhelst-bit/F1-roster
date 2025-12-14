\# F1 Team Roster (Python CLI)



\## Beschrijving



Deze applicatie is een \*\*command-line tool\*\* geschreven in \*\*Python\*\* waarmee F1-teams en hun rijders beheerd kunnen worden.

De data wordt opgeslagen in een \*\*SQLite-database\*\*. Via de terminal kan de gebruiker:



\* F1-teams toevoegen

\* F1-rijders toevoegen (gekoppeld aan een team)

\* Teams exporteren naar CSV

\* Rijders exporteren naar CSV



Dit project is ontwikkeld als opdracht voor het vak \*\*Python\*\* en voldoet aan alle opgelegde vereisten.



---



\## Projectstructuur



F1-roster/

│

├── app/

│   ├── \_\_init\_\_.py

│   ├── main.py          # Startpunt van de applicatie

│   ├── database.py      # SQLite connectie en tabellen

│   └── models.py        # Klassen (Team, Driver)

│

├── config/

│   └── settings.example.ini

│

├── data/

│   └── f1\_roster.db     # SQLite database (sample data)

│

├── README.md

├── requirements.txt

└── .gitignore

```

---



\## Vereisten



\* Python 3.10 of hoger

\* Git



Alle dependencies worden geïnstalleerd via `requirements.txt`.



---



\## Installatie \& Setup



Volg deze stappen \*\*exact\*\* (zoals de docent dit zal doen):



\### Repository clonen



```bash

git clone https://github.com/ricardoverhelst-bit/F1-roster.git

cd F1-roster

```



\### Virtual environment aanmaken



```bash

python -m venv venv

```



\### Virtual environment activeren



\*\*Windows:\*\*



```bash

venv\\Scripts\\activate

```

Je ziet nu `(venv)` voor je terminalprompt.



---



\### Dependencies installeren



```bash

pip install -r requirements.txt

```



---



\## Applicatie starten



De applicatie wordt gestart vanuit de \*\*rootmap\*\* met:



```bash

python -m app.main

```



---



\##Gebruik van de applicatie



Bij het starten verschijnt het volgende menu:



```

F1 TEAM ROSTER

1\. Team toevoegen

2\. Driver toevoegen

3\. Exporteer teams naar CSV

4\. Exporteer drivers naar CSV

0\. Afsluiten

```



\### Team toevoegen



\* Vraagt teamnaam en land

\* Wordt opgeslagen in de database



\### Driver toevoegen



\* Vraagt naam, rugnummer en team\_id

\* Driver wordt gekoppeld aan een team



\### CSV export



\* `teams.csv` → alle teams

\* `drivers.csv` → alle drivers



CSV-bestanden worden aangemaakt in de hoofdmap van het project.



---



\## Database



De applicatie gebruikt een \*\*SQLite database\*\* (`data/f1\_roster.db`) met twee tabellen:



\### `teams`



| Kolom   | Type         |

| ------- | ------------ |

| id      | INTEGER (PK) |

| name    | TEXT         |

| country | TEXT         |



\### `drivers`



| Kolom   | Type                    |

| ------- | ----------------------- |

| id      | INTEGER (PK)            |

| name    | TEXT                    |

| number  | INTEGER                 |

| team\_id | INTEGER (FK → teams.id) |



De tabel `sqlite\_sequence` wordt automatisch door SQLite aangemaakt.



---



\## Klassen



De applicatie gebruikt Python-klassen in `models.py`:



\* `Team`

\* `Driver`



Deze klassen vertegenwoordigen de entiteiten uit de database.



---



\## Configuratie \& veiligheid



\* De database staat \*\*niet hardcoded\*\* in de code

\* Gevoelige bestanden zoals:



&nbsp; \* `venv/`

&nbsp; \* `settings.ini`

&nbsp; \* `\_\_pycache\_\_/`



worden uitgesloten via `.gitignore`



Een voorbeeldconfiguratie is beschikbaar in:



```

config/settings.example.ini

```



---



\## Git \& versiebeheer



\* Ontwikkeling gebeurde met \*\*Git\*\*

\* Meerdere duidelijke commits

\* Correcte `.gitignore`

\* Publieke GitHub repository



---



\## Auteur



Naam: Ricardo Verhelst

Opleiding: Bachelor Cybersecurity

Vak: Python



---



\## Status



Opdracht volledig geïmplementeerd



