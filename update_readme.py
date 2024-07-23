import os
import random
from datetime import datetime

def get_random_image(images_dir: str):
    images = os.listdir(images_dir)
    return random.choice(images)

def update_readme(image_filename: str, img_id: str, height:int):
    readme_path = 'README.md'
    
    # Leer el contenido actual del README.md
    with open(readme_path, 'r', encoding='utf-8') as readme_file:
        lines = readme_file.readlines()
    
    # Buscar y reemplazar la línea de la imagen
    with open(readme_path, 'w', encoding='utf-8') as readme_file:
        for line in lines:
            if f'id="{img_id}"' in line:
                # Reemplaza la línea con la nueva imagen
                new_line = f'    <img id="{img_id}" src="{image_filename}" height="{height}px" />\n'
                readme_file.write(new_line)
            else:
                readme_file.write(line)

if __name__ == "__main__":
    random_image = get_random_image(images_dir='images/backgrounds')
    update_readme(image_filename=f"./images/backgrounds/{random_image}", img_id='Random_Images', height=400)

    daily_quoutes = get_random_image(images_dir='images/daily_quotes')
    update_readme(image_filename=f"./images/daily_quotes/{daily_quoutes}", img_id='Random_Quoutes', height=200)

    os.system("git config --global user.email thomas.molina.s@mail.pucv.cl")
    os.system("git config --global user.name Thomas Molina")
    os.system("git add .")
    commit_message = f"Update daily image on {datetime.now().strftime('%Y-%m-%d')}"
    os.system(f"git commit -m \"{commit_message}\"")
    os.system("git push")
