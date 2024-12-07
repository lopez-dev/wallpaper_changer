# Wallpaper Changer

Dieses Python-Skript ermöglicht es, den Desktop-Hintergrund auf Windows-Computern zufällig aus einem angegebenen Ordner zu ändern.

## Inhaltsverzeichnis

1. [Voraussetzungen](#voraussetzungen)
2. [Installation](#installation)
3. [Konfiguration](#konfiguration)
4. [Verwendung](#verwendung)
5. [Kompilierte Version](#kompilierte-version)
6. [Unterschiede zur Windows-Diashow-Funktion](#unterschiede-zur-windows-diashow-funktion)
7. [Funktionen](#funktionen)
8. [Fehlerbehebung](#fehlerbehebung)
9. [Lizenz](#lizenz)

---

## Voraussetzungen

- Python 3.x
- Windows-Betriebssystem

---

## Installation

1. Klonen Sie das Repository oder laden Sie es als ZIP-Datei herunter und entpacken Sie es.
2. Stellen Sie sicher, dass Python 3.x auf Ihrem System installiert ist.

---

## Konfiguration

Erstellen Sie eine `config.ini`-Datei im selben Verzeichnis wie das Skript mit folgendem Inhalt:

```ini
[Settings]
folder_path = Pfad/zum/Bilderordner
```

Ersetzen Sie `Pfad/zum/Bilderordner` durch den vollständigen Pfad zu dem Ordner, der die Hintergrundbilder enthält.

---

## Verwendung

Führen Sie das Skript mit folgendem Befehl in der Konsole aus:

```bash
python wallpaper_changer.py
```

Das Skript führt die folgenden Schritte aus:
1. Es lädt die Konfigurationsdaten aus der `config.ini`.
2. Es wählt ein zufälliges Bild aus dem angegebenen Ordner.
3. Es setzt das Bild als Desktop-Hintergrund.

---

## Kompilierte Version

Eine kompilierte Version des Skripts befindet sich im `dist`-Ordner. Sie kann wie folgt verwendet werden:
1. Kopieren Sie die ausführbare Datei (`.exe`) in einen beliebigen Ordner.
2. Platzieren Sie die `config.ini`-Datei im selben Verzeichnis und passen Sie den Pfad zu den Bildern an.
3. Sie können die ausführbare Datei über den **Aufgabenplaner von Windows** regelmäßig ausführen lassen.

### Hinweis für den Aufgabenplaner

Damit das Skript die `config.ini`-Datei lesen kann:
1. Geben Sie im Aufgabenplaner unter **"Starten in (optional)"** den Ordnerpfad ein, in dem die `.exe`-Datei und die `config.ini` gespeichert sind.
2. Ohne diese Angabe wird das Skript möglicherweise nicht korrekt ausgeführt, da die `config.ini` nicht gefunden wird.

Beispiel:
- **Programm/Skript**: `C:\Pfad\zum\script.exe`
- **Starten in (optional)**: `C:\Pfad\zum`

---

## Unterschiede zur Windows-Diashow-Funktion

Im Gegensatz zur standardmäßigen Diashow-Funktion von Windows:
- Ändert dieses Skript das gleiche Hintergrundbild auf allen Monitoren.
- Der Wechsel erfolgt ohne visuelle Effekte.

---

## Funktionen

### `load_config(config_file)`
Lädt die Konfigurationsdaten aus einer `.ini`-Datei. Diese Funktion prüft die Datei auf folgende Parameter:
- `folder_path`: Der Pfad zum Ordner mit den Bildern.

### `change_wallpaper_to_next(folder_path)`
Wählt ein zufälliges Bild aus dem angegebenen Ordner und setzt es als Desktop-Hintergrund. Unterstützte Bildformate sind:
- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`

---

## Fehlerbehebung

Falls das Skript nicht wie erwartet funktioniert:
1. **Überprüfen Sie den Pfad in der `config.ini`.** 
   Stellen Sie sicher, dass der angegebene Ordner existiert und erreichbar ist.
2. **Prüfen Sie den Ordnerinhalt.** 
   Stellen Sie sicher, dass der Ordner gültige Bilddateien enthält.
3. **Aufgabenplaner-Einstellungen prüfen.** 
   Vergewissern Sie sich, dass der Pfad unter **"Starten in (optional)"** korrekt ist.

---

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz veröffentlicht. Weitere Informationen finden Sie in der `LICENSE`-Datei des Projekts.

---
```