# Script para edición de archivos y movimientos entre carpetas.

Este es un pequeño script en python para ordenar archivos cbz, pudiendo quitar las etiquetas de su nombre y meterlos en carpetas respectivas.

Además de otro script para extraer el archivo info.json y la primera imagen del mismo archivo, genera los archivos legibles por apps como mihon o similares.

Está pensado para funcionar en Windows y considerando mis necesidades del momento, no planeo darle mucho soporte, pero aquí queda por si le sirve a alguien de futuro.

## modificaciones_archivo.py

Este script es el que modifica el nombre y mete en carpetas separadas, no cataloga por series, pero puede permitirte generar cierto orden ya que extrae cualquier etiqueta [] o () dentro del nombre.

Ejemplo:

> [autor(publisher)] Nombre de manga (Revista).cbz

quedaría como 

> Nombre de manga.cbz

es posible ejecutar el script de la siguiente manera:

> python modificaciones_archivo.py

Para Modificar nombres, crear carpetas y mover los archivos a su respectiva carpeta.

> python modificaciones_archivo.py --edit

Solo modifica los archivos cbz dentro de la ruta donde esté el script.

## extractor_json_y_cover.py

Script para extraer info.json y cover de todos los archivos cbz dentro de las subcarpetas creadas anteriormente.

No necesita argumentos, para ejecutarlo hay que meter el archivo en la carpeta local donde tienes tus comics/mangas/cualquier otro y ejecutarlo:

> python extractor_json_y_cover.py

El extractor hará su trabajo.