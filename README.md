# Erweiterung und Debugging einer TODO-App mit Flask und API-Integration

## **Beschreibung**
Du arbeitest an einer kleinen TODO-App, die Benutzereingaben über ein Formular sammelt und mithilfe einer öffentlichen API ([JSONPlaceholder](https://jsonplaceholder.typicode.com/)) verarbeitet. Ziel ist es, die Anwendung zu verstehen, zu erweitern und eine neue Funktionalität zu implementieren.

---

## **Bearbeitungszeit**
**ca. 20 Minuten**

---

## **Aufgaben**

### **Aufgabe 1: Verständnis der bestehenden Anwendung**
- **Erkläre:** Wie funktioniert die bestehende Anwendung?  
- **Beschreibung:** Beschreibe die Schritte vom Absenden eines Formulars bis zur Anzeige der API-Antwort.  
  Ziel ist es, die grundlegende Funktionsweise von Frontend, Backend und der API-Integration zu verstehen.

---

### **Aufgabe 2: Erweiterung des Formulars**
- **Füge die folgenden neuen Felder zum Formular hinzu:**
  1. **Priorität:** Eine Dropdown-Auswahl (z. B. Hoch, Mittel, Niedrig).
  2. **Datum:** Ein Datumsfeld.
  
- **Anforderungen:**
  - Die neuen Felder sollen:
    1. Im Formular angezeigt werden.
    2. Die Werte sollen mit den anderen Eingabedaten (`userId`, `title`, `completed`) an die API gesendet werden.

---

### **Aufgabe 3: Anzeige aller TODOs**
- **Implementiere eine neue Funktion:**
  - Rufe die vorhandenen TODO-Einträge aus der API (`GET /todos`) ab.
  - Zeige die Ergebnisse im Frontend in einer übersichtlichen Liste an.

---

## **Anleitung zur Nutzung**

### **Voraussetzungen**
- Python 3.x installiert
- Abhängigkeiten installieren:
  ```bash
  pip install -r requirements.txt
