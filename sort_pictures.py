import os
import shutil
from datetime import datetime
import exifread
import tkinter as tk
from tkinter import filedialog

def sort_files(picture_folder):
    for file in os.listdir(picture_folder):
        file_pfad = os.path.join(picture_folder, file)
        if os.path.isfile(file_pfad):
            creation_date = get_creation_date(file_pfad)
            if creation_date:
                target_folder = os.path.join(picture_folder, creation_date.strftime("%Y-%m-%d"))
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                shutil.move(file_pfad, target_folder)

def get_creation_date(file_pfad):
    try:
        if file_pfad.lower().endswith((".jpg", ".jpeg", ".png", ".arw", ".mp4")):
            with open(file_pfad, 'rb') as picture_file:
                tags = exifread.process_file(picture_file, stop_tag='EXIF DateTimeOriginal')
                creation_date_str = str(tags.get('EXIF DateTimeOriginal'))
                creation_date = datetime.strptime(creation_date_str, '%Y:%m:%d %H:%M:%S')
                return creation_date
    except Exception as e:
        print(f"Error reading creation date {file_pfad}: {e}")
        return None

def choose_folder():
    picture_folder = filedialog.askdirectory()
    if picture_folder:
        sort_files(picture_folder)
        print("Pictures sorted.")

def main():
    root = tk.Tk()
    root.withdraw()

    # Erstellen der UI
    ui = tk.Tk()
    ui.title("Bilder sortieren")

    # Funktion für den Button
    def select_folder():
        choose_folder()

    # Button erstellen
    button = tk.Button(ui, text="Ordner auswählen", command=select_folder)
    button.pack(pady=20)

    ui.mainloop()

if __name__ == "__main__":
    main()
