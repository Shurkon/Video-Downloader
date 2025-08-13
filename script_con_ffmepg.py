#!/usr/bin/env python3

# Importar la librería 

import yt_dlp


# Función principal

def descargar_video(url):
    opciones = {
        "format": "bestvideo+bestaudio/best",  # Máxima calidad disponible
        "merge_output_format": "mp4",          # Unificar en MP4 después de descargar
        "outtmpl": "videos/%(title)s.%(ext)s", # Carpeta y nombre automáticos
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


# Flujo del programa

if __name__ == "__main__":
    enlace = input("Introduce la URL del video: ")
    descargar_video(enlace)
