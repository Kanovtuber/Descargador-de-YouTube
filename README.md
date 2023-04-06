# Descargador de YouTube

Esta aplicación de escritorio permite descargar videos de YouTube con diferentes calidades de video o solo el audio. Está desarrollada en Python utilizando la biblioteca `tkinter` para la interfaz gráfica y la biblioteca `pytube` para la descarga de videos.

## Requisitos previos

- Python 3.6 o superior instalado en el sistema.

## Instalación

1. Clona o descarga el repositorio de GitHub en tu PC:

   ```bash
   git clone https://github.com/Kanovtuber/Descargador-de-YouTube.git
Si no tienes git instalado, también puedes descargar el repositorio como un archivo ZIP y extraerlo en tu PC.

Abre la terminal y navega al directorio donde se encuentra el repositorio clonado o extraído.

Instala las dependencias necesarias:
pip install pytube tkinter
## Ejecución
Ejecuta el script principal descargador_youtube_gui.py: python descargador_youtube_gui.py

Esto abrirá la ventana de la aplicación Descargador de YouTube.

Ingresa la URL del video de YouTube que deseas descargar en el campo "URL del video".

Selecciona la ruta de guardado haciendo clic en "Seleccionar ruta" y eligiendo una carpeta en tu PC.

Selecciona la calidad del video (Baja, Media o Máxima) en el menú desplegable "Calidad".

Si deseas descargar solo el audio, marca la casilla "Descargar solo audio".

Haz clic en "Descargar video" para iniciar la descarga.
