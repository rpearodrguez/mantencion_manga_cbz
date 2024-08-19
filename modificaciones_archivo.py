# Script que edita el nombre de un archivo, quitando el contenido entre paréntesis y corchetes.
# Crea una carpeta para cada archivo con el nombre modificado y mueve el archivo a la carpeta correspondiente.{
# El script funciona en la ruta en la que se encuentran los archivos a modificar.

import os
import re
import shutil
import time
import sys

# Función que crea una carpeta con el nombre del archivo modificado y mueve el archivo a la carpeta.
def crear_carpeta_y_mover_archivo(ruta_archivo, nueva_ruta, nombre_archivo ):
    # Crear carpeta con el nuevo nombre del archivo.
    # Verificar si la carpeta no existe.
    if not os.path.exists(nueva_ruta):
        os.mkdir(nueva_ruta)
        print('Carpeta creada exitosamente.')
    else:
        print('La carpeta {} ya existe.'.format(nueva_ruta))
    # Descansa por 1 segundo.
    time.sleep(1)
    # Mover archivo a la carpeta.
    shutil.move(nombre_archivo, nueva_ruta + '/' + nombre_archivo)
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
    nueva_ruta = re.sub(patron, '', nombre_archivo_sin_extension).strip()
    nueva_carpeta = os.path.join(os.path.dirname(ruta_archivo), nueva_ruta)
    # Cambia nombre de archivo
    nuevo_nombre = os.path.join(os.path.dirname(ruta_archivo), nueva_ruta + os.path.splitext(nombre_archivo)[1])
    os.rename(nombre_archivo, nuevo_nombre)
    # Vuelve a obtener la ruta del archivo con el nuevo nombre.
    ruta_archivo_2 = os.path.abspath(nuevo_nombre + os.path.splitext(nombre_archivo)[1])
    # Si el argumento es --create o no se pasa argumento, crea carpeta con el nuevo nombre del archivo y mueve el archivo a la carpeta.
    if len(sys.argv) == 1:
        # Crear carpeta con el nuevo nombre del archivo y mover el archivo a la carpeta.
        print('Creando carpeta y moviendo archivo:', nuevo_nombre)
        crear_carpeta_y_mover_archivo(nueva_ruta, nueva_carpeta, nuevo_nombre)


if __name__ == '__main__':
    opcion = ''
    if len(sys.argv) == 1:
        print('Modificando archivos...')
        # Obtener la lista de archivos en la ruta actual.
        archivos = os.listdir()
        # Recorrer la lista de archivos.
        for archivo in archivos:
            # Verificar si el archivo es un archivo su extensión es cbz
            if os.path.isfile(archivo) and archivo.endswith('.cbz'):
                # Editar el nombre del archivo.
                editar_nombre_archivo(archivo)
        print('Archivos modificados exitosamente.')
    elif sys.argv[1] == '--edit':
        opcion = sys.argv[1]
        print('Modificando archivos...')
        # Obtener la lista de archivos en la ruta actual.
        archivos = os.listdir()
        # Recorrer la lista de archivos.
        for archivo in archivos:
            # Verificar si el archivo es un archivo su extensión es cbz
            if os.path.isfile(archivo) and archivo.endswith('.cbz'):
                # Editar el nombre del archivo.
                editar_nombre_archivo(archivo)
        print('Archivos modificados exitosamente.')
    else:
        print('Modificaciones Archivo')
        print('Script que edita el nombre de un archivo, quitando el contenido entre paréntesis y corchetes.')
        print('Crea una carpeta para cada archivo con el nombre modificado y mueve el archivo a la carpeta correspondiente.')
        print('El script funciona en la ruta en la que se encuentran los archivos a modificar.')
        print('Uso: python modificaciones_archivo.py')
        print('-------------------------------------------------')
        print('Es posible ejecutar el script en la terminal de la siguiente manera:')
        print('python modificaciones_archivo.py --edit')
        print('para editar los nombres de los archivos en la ruta actual.')
        print('-------------------------------------------------')
        


# Fin del script.