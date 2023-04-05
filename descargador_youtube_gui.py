import tkinter as tk
from tkinter import ttk, filedialog
from pytube import YouTube

def on_progress_do(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = (size - bytes_remaining) / size
    barra_progreso['value'] = progress * 100
    ventana.update_idletasks()

def descargar_video(url, ruta_guardado, calidad, solo_audio):
    try:
        video = YouTube(url, on_progress_callback=on_progress_do)
        
        if solo_audio:
            stream = video.streams.filter(only_audio=True).first()
            ext = ".mp3"
        else:
            if calidad == "Baja":
                stream = video.streams.filter(progressive=True).order_by('resolution').first()
            elif calidad == "Media":
                stream = video.streams.filter(progressive=True).order_by('resolution').all()[1]
            else:
                stream = video.streams.get_highest_resolution()

            ext = ".mp4"

        archivo = f"{video.title}{ext}"
        archivo = archivo.replace('/', '').replace('\\', '').replace(':', '').replace('*', '').replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')
        stream.download(ruta_guardado, filename=archivo)
        mensaje.set("Video descargado exitosamente.")
    except Exception as e:
        mensaje.set(f"Error al descargar el video: {e}")

def seleccionar_ruta():
    ruta = filedialog.askdirectory()
    ruta_guardado.set(ruta)

def iniciar_descarga():
    url_video = url.get()
    ruta = ruta_guardado.get()
    calidad = calidad_video.get()
    solo_audio = var_solo_audio.get()
    descargar_video(url_video, ruta, calidad, solo_audio)

ventana = tk.Tk()
ventana.title("Descargador de YouTube")

url = tk.StringVar()
ruta_guardado = tk.StringVar()
calidad_video = tk.StringVar()
var_solo_audio = tk.BooleanVar()
mensaje = tk.StringVar()

calidad_video.set("Máxima")

tk.Label(ventana, text="URL del video:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
tk.Entry(ventana, textvariable=url, width=50).grid(row=0, column=1, padx=10, pady=10)

tk.Label(ventana, text="Ruta de guardado:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
tk.Entry(ventana, textvariable=ruta_guardado, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(ventana, text="Seleccionar ruta", command=seleccionar_ruta).grid(row=1, column=2, padx=10, pady=10)

tk.Label(ventana, text="Calidad:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
tk.OptionMenu(ventana, calidad_video, "Baja", "Media", "Máxima").grid(row=2, column=1, padx=10, pady=10, sticky="w")

tk.Checkbutton(ventana, text="Descargar solo audio", variable=var_solo_audio).grid(row=3, column=1, padx=10, pady=10, sticky="w")

tk.Button(ventana, text="Descargar video", command=iniciar_descarga).grid(row=4, column=1, padx=10, pady=10)

barra_progreso = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="determinate")
barra_progreso.grid(row=5, column=1, padx=10, pady=10)

tk.Label(ventana, textvariable=mensaje).grid(row=6, column=1, padx=10, pady=10)

ventana.mainloop()
