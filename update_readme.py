import os
import random

def get_random_image(images_dir: str):
    images = os.listdir(images_dir)
    return random.choice(images)

def update_readme(image_filename: str, img_id: str, height:int):
    readme_path = 'README.md'
    
    # Leer el contenido actual del README.md
    with open(readme_path, 'r') as readme_file:
        lines = readme_file.readlines()
    
    # Buscar y reemplazar la línea de la imagen
    with open(readme_path, 'w') as readme_file:
        for line in lines:
            if f'id="{img_id}"' in line:
                # Reemplaza la línea con la nueva imagen
                new_line = f'    <img id="{img_id}" src="{image_filename}" height="{height}px" />\n'
                readme_file.write(new_line)
            else:
                readme_file.write(line)

if __name__ == "__main__":
    random_image = get_random_image(images_dir='images/backgrounds')
    update_readme(image_filename=random_image, img_id='Random_Images', height=400)

    daily_quoutes = get_random_image(images_dir='images/daily_quotes')
    update_readme(image_filename=daily_quoutes, img_id='Random_Quoutes', height=200)
