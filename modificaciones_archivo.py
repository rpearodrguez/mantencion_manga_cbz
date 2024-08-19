# Script que edita el nombre de un archivo, quitando el contenido entre paréntesis y corchetes.
# Crea una carpeta para cada archivo con el nombre modificado y mueve el archivo a la carpeta correspondiente.{
# El script funciona en la ruta en la que se encuentran los archivos a modificar.

import os
import re
import shutil

# Función que crea una carpeta con el nombre del archivo modificado y mueve el archivo a la carpeta.
def crear_carpeta_y_mover_archivo(ruta_archivo, nombre_archivo, nuevo_nombre):
    # Crear carpeta con el nuevo nombre del archivo.
    os.mkdir(nuevo_nombre)
    # Mover archivo a la carpeta.
    shutil.move(ruta_archivo, nuevo_nombre + '/' + nombre_archivo)
    print('Archivo movido exitosamente.')

# Función que edita el nombre del archivo, quitando el contenido entre paréntesis y corchetes.
def editar_nombre_archivo(ruta_archivo):
    # Obtener el nombre del archivo.
    nombre_archivo = os.path.basename(ruta_archivo)
    # Obtener el nombre del archivo sin la extensión.
    nombre_archivo_sin_extension = os.path.splitext(nombre_archivo)[0]
    # Patrón para encontrar el contenido entre paréntesis y corchetes.
    patron = re.compile(r'\[.*?\]|\(.*?\)')
    # Editar el nombre del archivo, quitando el contenido entre paréntesis y corchetes.
    nuevo_nombre = re.sub(patron, '', nombre_archivo_sin_extension).strip()
    # Crear carpeta con el nuevo nombre del archivo y mover el archivo a la carpeta.
    print('Creando carpeta y moviendo archivo:', nuevo_nombre)
    crear_carpeta_y_mover_archivo(ruta_archivo, nombre_archivo, nuevo_nombre)

# Obtener la lista de archivos en la ruta actual.
archivos = os.listdir()
# Recorrer la lista de archivos.
for archivo in archivos:
    # Verificar si el archivo es un archivo.
    if os.path.isfile(archivo):
        print('Editando el archivo:', archivo)
        # Editar el nombre del archivo.
        editar_nombre_archivo(archivo)

print('Archivos modificados exitosamente.')

# Fin del script.