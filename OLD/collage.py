
from PIL import Image
import random
import os

background_path = "background.jpg"

def create_collages(background_path, objects_folder, coordinates, output_folder, num_images=6):
    # Carica l'immagine di background
    background = Image.open(background_path)

    # Elenco di tutte le immagini degli oggetti
    object_images = [img for img in os.listdir(objects_folder) if img.endswith('.jpg')]

    # Assicurati che ci siano almeno 2 immagini e non più di 120
    if not 2 <= len(object_images) <= 6:
        raise ValueError("Il numero di immagini degli oggetti deve essere tra 2 e 6.")

    # Genera 100 combinazioni uniche di coppie di immagini
    all_combinations = random.sample([(i, j) for i in object_images for j in object_images if i != j], num_images)

    # Crea le immagini collage
    for idx, (img1, img2) in enumerate(all_combinations, 1):
        with Image.open(os.path.join(objects_folder, img1)) as obj1, Image.open(os.path.join(objects_folder, img2)) as obj2:
            # Crea una copia del background per ogni collage
            temp_background = background.copy()

            # Posiziona le immagini degli oggetti sul background
            temp_background.paste(obj1, coordinates[0], obj1)
            temp_background.paste(obj2, coordinates[1], obj2)

            # Salva il collage
            temp_background.save(os.path.join(output_folder, f'img_{idx:03}.jpg'))

# Esempio di come chiamare la funzione
create_collages('background.jpg', 'objects_folder', [(0, 220), (200, 220)], 'output_folder')


