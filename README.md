# devcontainer-demo

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/fhswf/devcontainer-demo?quickstart=1)

1. Auf den Link klicken und ca. 2 Minuten warten
2. Im Terminal: `pytest -v`  → startet PostgreSQL im Container, testet, löscht ihn
3. Im Terminal: `uvicorn main:app --reload --port 8000` → Web-App öffnet sich
4. Danach: Codespace stoppen (github.com/codespaces), sonst läuft das Kontingent weiter
