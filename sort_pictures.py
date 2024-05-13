import os
import shutil
from datetime import datetime
import exifread

# Pfad zum Ordner mit den Bildern
bilder_ordner = "Path/to/explorer/folder"

def sortiere_dateien():
    for datei in os.listdir(bilder_ordner):
        if datei.lower().endswith((".jpg", ".jpeg", ".png", ".arw", ".mp4")):
            datei_pfad = os.path.join(bilder_ordner, datei)
            aufnahmedatum = get_aufnahmedatum(datei_pfad)
            if aufnahmedatum:
                ziel_ordner = os.path.join(bilder_ordner, aufnahmedatum.strftime("%Y-%m-%d"))
                if not os.path.exists(ziel_ordner):
                    os.makedirs(ziel_ordner)
                shutil.move(datei_pfad, ziel_ordner)

def get_aufnahmedatum(datei_pfad):
    try:
        if datei_pfad.lower().endswith((".jpg", ".jpeg", ".png", ".arw")):
            with open(datei_pfad, 'rb') as bild_datei:
                tags = exifread.process_file(bild_datei, stop_tag='EXIF DateTimeOriginal')
                aufnahmedatum_str = str(tags.get('EXIF DateTimeOriginal'))
                aufnahmedatum = datetime.strptime(aufnahmedatum_str, '%Y:%m:%d %H:%M:%S')
                return aufnahmedatum
        elif datei_pfad.lower().endswith(".arw"):
            # Hier könntest du rawpy verwenden, um das Aufnahmedatum aus den Metadaten der RAW-Datei zu extrahieren
            pass
        elif datei_pfad.lower().endswith(".mp4"):
            # Hier könntest du eine Bibliothek verwenden, um das Aufnahmedatum aus den Metadaten der MP4-Datei zu extrahieren
            pass
        else:
            # Fallback: Verwende das Änderungsdatum
            return datetime.fromtimestamp(os.path.getmtime(datei_pfad))
    except Exception as e:
        print(f"Fehler beim Lesen des Aufnahmedatums von {datei_pfad}: {e}")
        return None

if __name__ == "__main__":
    sortiere_dateien()
    print("Dateien wurden sortiert.")