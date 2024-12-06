Titel:
Erweiterung und Debugging einer TODO-App mit Flask und API-Integration

Beschreibung:
Du arbeitest an einer kleinen TODO-App, die Benutzereingaben über ein Formular sammelt und mithilfe einer öffentlichen API (JSONPlaceholder) verarbeitet. Ziel ist es, die Anwendung zu verstehen, zu erweitern und eine neue Funktionalität zu implementieren.

Bearbeitungszeit:
ca. 20 Minuten

Aufgaben:

Aufgabe 1: Verständnis der bestehenden Anwendung
Erkläre: Wie funktioniert die bestehende Anwendung? Beschreibe die Schritte vom Absenden eines Formulars bis zur Anzeige der API-Antwort.

Aufgabe 2: Erweiterung des Formulars
Füge die folgenden neuen Felder zum Formular hinzu:
- Priorität: Eine Dropdown-Auswahl (z. B. Hoch, Mittel, Niedrig).
- Datum: Ein Datumsfeld.

Anforderungen:
Die neuen Felder sollen:
Im Formular angezeigt werden.
Die Werte sollen mit den anderen Eingabedaten (userId, title, completed) an die API gesendet werden.

Aufgabe 4: Anzeige aller TODOs
Implementiere eine Funktion, die die vorhandenen TODO-Einträge aus der API (GET /todos) abruft und im Frontend anzeigt.
