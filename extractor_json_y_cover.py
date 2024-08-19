# Accede a cada carpeta en la ruta del script, accede al archivo cbz y extrae los archivos info.json y 01.png.
# Guarda el archivo info.json en la carpeta de la serie correspondiente con el nombre details.json
# Guarda primer archivo .png en la carpeta de la serie correspondiente con el nombre cover.jpg
# Si el archivo details.json ya existe, lo sobreescribe.

import os
import zipfile
import json

#

# Función que extrae el archivo info.json de un archivo cbz, si existe más de un archivo cbz en la carpeta, se mezclarán los datos de los archivos info.json
def extraer_info(archivo):
    print('Extrayendo info', archivo)
    with zipfile.ZipFile(archivo, 'r') as zip_ref:
        for name in zip_ref.namelist():
            if name.endswith('info.json'):
                zip_ref.extract(name, 'temp')
                with open('temp/' + name, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # Si el archivo details.json ya existe, se agregan los datos del archivo como contenido extra al final de su etiqueta
                    if os.path.exists(os.path.join(os.path.dirname(archivo), 'details.json')):
                        with open(os.path.join(os.path.dirname(archivo), 'details.json'), 'r') as f:
                            data2 = json.load(f)
                            for k, v in data.items():
                                if k in data2:
                                    # Si el campo es Tags, se mantiene como lista
                                    if k == 'Tags' or k == 'Genre':
                                        data2[k].extend(v)
                                    # Si el campo es una lista, se convierte a string y se agrega el nuevo valor
                                    elif type(data2[k]) == list:
                                        data2[k].extend(str(v))
                                    else:
                                        data2[k] = [data2[k], v]
                                else:
                                    data2[k] = v
                            data = data2
                    with open(os.path.join(os.path.dirname(archivo), 'details.json'), 'w') as f:
                        json.dump(data, f, indent=4)
                break
    return

# Funcion que procesa el archivo info.json para eliminar los campos que no se necesitan
def procesar_info(archivo):
    # Abre el archivo details.json
    with open(archivo, 'r') as f:
        data = json.load(f)
        # Si no existe el campo Description, se utiliza el campo Magazine, si no existe Magazine se utiliza un string con el formato "Artist - Title"
        if 'Description' not in data:
            if 'Magazine' in data:
                data['Description'] = data['Magazine']
            else:
                # Si no existe el campo Magazine, se agrega el campo Description con el formato ["Artist - Title"]
                data['Description'] = data['Artist'][0] + ' - ' + str(data['Title'][0])
        # Si no existe el campo Author, se utiliza el campo Artist
        if 'Author' not in data:
            data['Author'] = data['Artist']
        # Se convierte el campo Tags a genre
        if 'Tags' in data:
            data['Genre'] = data['Tags']
        # Se convierten las claves a minúsculas
        data = {k.lower(): v for k, v in data.items()}
        # Solo se guardan los campos: title, author, artist, description, genre
        data = {k: v for k, v in data.items() if k in ['title', 'author', 'artist', 'description', 'genre']}
        # Recorre todos los campos y si son listas, las convierte a strings, 
        # si todos los elementos de la lista son iguales, se guarda un solo elemento
        for k, v in data.items():
            # Si el es el campo genre, se mantiene como lista, pero se quitan elementos duplicados
            if k == 'genre':
                data[k] = list(set(v))
            else:
            # Para el resto de campos, si es una lista, se usa el primer elemento como string, y se le quitan los números
                if type(v) == list:
                    data[k] = str(v[0])
                    data[k] = ''.join([i for i in data[k] if not i.isdigit()])
            
        # Guarda los datos procesados en el archivo details.json
        with open(archivo, 'w') as f:
            json.dump(data, f, indent=4)
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
                # Si hay más de un archivo cbz en la carpeta, extrae la info de todos los archivos y luego la procesa
                if len(files) > 1:
                    for archivo in files:
                        if archivo.endswith('.cbz'):
                            extraer_info(os.path.join(root, archivo))
                            extraer_portada(os.path.join(root, archivo))
                else:
                    extraer_info(os.path.join(root, name))
                # Procesa el archivo details.json
                procesar_info(os.path.join(root, 'details.json'))
    return



recorrer_carpetas()