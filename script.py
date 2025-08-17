#!/usr/bin/env python3

# Importar la librería 

import yt_dlp


# Función principañ

def main():

        
    print("\n[+] Por favor, selecciona una de las siguientes opciones: \n")
    print("\n[1] Descargar video a baja resolución")
    print("[2] Descargar video a alta resolución (Requiere tener instalado ffmepg)")
    print("[3] Descargar audio mp3")
    print("[4] Descargar audio mp4")


    while True:   
        
        opcion = int(input("\n\t Tu opción(1-4) --> "))
        
        if opcion == 1:

            print("\n\n[i] Has elegido la opción nº1")
            enlace = input("[+] Introduce la URL del video: ")
            opcion1(enlace)
            break

        elif opcion == 2:

            print("\n\n[i] Has elegido la opción nº2")
            enlace = input("[+] Introduce la URL del video: ")
            opcion2(enlace)
            break

        elif opcion == 3:

            print("\n\n[i] Has elegido la opción nº3")
            enlace = input("[+] Introduce la URL del video: ")
            opcion3(enlace)
            break

        elif opcion == 4:

            print("\n\n[i] Has elegido la opción nº4")
            enlace = input("[+] Introduce la URL del video: ")
            opcion4(enlace)
            break

        else:

            print("\n\n[!] La opción que has elegido no existe")


# Funciones

def opcion1(url):
    opciones = {
        "outtmpl": f"videos/%(title)s.%(ext)s",  # Carpeta y nombre automáticos
        "format": "best",                                  # Máxima calidad disponible
        "merge_output_format": "mp4",                      # Unificar en MP4
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])



def opcion2(url):
    opciones = {
        "format": "bestvideo+bestaudio/best",  # Máxima calidad disponible
        "merge_output_format": "mp4",          # Unificar en MP4 después de descargar
        "outtmpl": "videos/%(title)s.%(ext)s", # Carpeta y nombre automáticos
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])



def opcion3(url):
    opciones = {
        "format": "bestaudio/best",               # Mejor calidad de audio disponible
        "outtmpl": "audios/%(title)s.%(ext)s",    # Carpeta y nombre automático
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",      # Extraer audio con FFmpeg
                "preferredcodec": "mp3",          # Convertir a mp3
                "preferredquality": "192",        # Calidad de audio
            }
        ],
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])



def opcion4(url):
    opciones = {
        "format": "bestaudio/best",              # Solo audio en la mejor calidad
        "outtmpl": "audios/%(title)s.%(ext)s",   # Carpeta y nombre automático
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",   # Convertir usando ffmpeg
                "preferedformat": "mp4",         # Guardar como .mp4
            }
        ],
    }

    with yt_dlp.YoutubeDL(opciones) as ydl:
        ydl.download([url])


# Flujo principal del programa


main()
