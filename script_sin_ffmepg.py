#!/usr/bin/env python3

# Importar modulos

import yt_dlp

# Función para descargar el video

def descargar_video(url, carpeta_salida="videos"):
    opciones = {
        "outtmpl": f"{carpeta_salida}/%(title)s.%(ext)s",  # Carpeta y nombre automático
        "format": "best",                                  # Máxima calidad disponible
        "merge_output_format": "mp4",                      # Unificar en MP4
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


# Pide el enlace del video

if __name__ == "__main__":
    enlace = input("Introduce la URL del video: ")
    descargar_video(enlace)
