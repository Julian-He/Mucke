Programm starten:

1. Repo klonen und in den Mucke-Ordner navigieren

2. Python Virtual-Environment aktivieren
   Windows (Powershell):
   `.venv\Scripts\Activate.ps1`
   Linux/Mac:
   `source .venv/bin/activate`

3. Programm starten
   `uvicorn main:api --reload`

Die Webapp ist nun über folgende Adresse aufrufbar:
`http://127.0.0.1:8000`
