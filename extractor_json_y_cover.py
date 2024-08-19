# Accede a cada carpeta en la ruta del script, accede al archivo cbz y extrae los archivos info.json y 01.png.
# Guarda el archivo info.json en la carpeta de la serie correspondiente con el nombre details.json
# Guarda primer archivo .png en la carpeta de la serie correspondiente con el nombre cover.jpg
# Si el archivo details.json ya existe, lo sobreescribe.

import os
import zipfile
import json

# Función que extrae el archivo info.json de un archivo cbz
def extraer_info(archivo):
    print('Procesando archivo', archivo)
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        print('Extrayendo info.json de', archivo)
        zip_ref.extract('info.json', 'temp')
    with open('temp/info.json', 'r', encoding='utf-8') as file:
        print('Guardando details.json en', os.path.dirname(archivo))
        info = json.load(file)
        with open(os.path.join(os.path.dirname(archivo), 'details.json'), 'w') as file:
            json.dump(info, file, indent=4)
    os.remove('temp/info.json')
    return

# Función que extrae el primer archivo .png o .jpg de un archivo cbz
def extraer_portada(archivo):
    print('Extrayendo portada', archivo)
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        for name in zip_ref.namelist():
            # Si archivo contiene 01, 001, 0001, etc. y termina en .png o .jpg
            if (name.find('01') != -1 or name.find('001') != -1 or name.find('0001') != -1) and (name.endswith('.png') or name.endswith('.jpg')):
                # Si el archivo ya existe, no lo sobreescribe
                if os.path.exists(os.path.join(os.path.dirname(archivo), 'cover.jpg')):
                    print('La portada ya existe en', os.path.dirname(archivo))
                    return
                zip_ref.extract(name, 'temp')
                os.rename('temp/' + name, os.path.join(os.path.dirname(archivo), 'cover.jpg'))
                break
    return    


    
# Función que recorre las carpetas de la ruta del script
def recorrer_carpetas():
    for root, dirs, files in os.walk(os.getcwd()):
        for name in files:
            if name.endswith('.cbz'):
                archivo = os.path.join(root, name)
                extraer_info(archivo)
                extraer_portada(archivo)
    return



recorrer_carpetas()