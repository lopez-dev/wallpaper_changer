import os
import ctypes
import random
import configparser

# Globale Variable für die Speicherung des zuletzt verwendeten Bilds
last_used_image = None

def load_config(config_file):
    """Lädt die Konfigurationsdaten aus einer .ini-Datei."""
    config = configparser.ConfigParser()
    config.read(config_file)

    try:
        folder_path = config.get("Settings", "folder_path")
        return folder_path
    except Exception as e:
        print(f"Fehler beim Laden der Konfiguration: {e}")
        return None

def change_wallpaper_to_next(folder_path):
    global last_used_image

    # Alle Bilddateien im Ordner finden und alphabetisch sortieren
    supported_extensions = ('.jpg', '.jpeg', '.png', '.bmp')
    image_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith(supported_extensions)])

    if not image_files:
        print("Keine gültigen Bilddateien im angegebenen Ordner gefunden.")
        return

    # Sicherstellen, dass ein anderes Bild ausgewählt wird
    available_images = [image for image in image_files if image != last_used_image]

    if not available_images:
        print("Alle Bilder wurden bereits verwendet. Starte erneut.")
        available_images = image_files.copy()

    # Zufälliges Bild auswählen
    next_image = random.choice(available_images)
    image_path = os.path.join(folder_path, next_image)

    # Hintergrund ändern
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
        print(f"Hintergrund erfolgreich geändert: {image_path}")
        last_used_image = next_image
    except Exception as e:
        print(f"Fehler beim Ändern des Hintergrunds: {e}")

if __name__ == "__main__":
    config_file = "config.ini"  # Name der Konfigurationsdatei

    # Konfiguration laden
    folder_path = load_config(config_file)

    if folder_path:
        change_wallpaper_to_next(folder_path)
    else:
        print("Bitte überprüfe die Konfigurationsdatei und starte das Programm erneut.")
