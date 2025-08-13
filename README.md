
¡Hola a todos! Aquí os paso un script en Python que he usado para descargar videos de YouTube. Os puede ser útil como alternativa a las webs para descargar videos que muy seguramente recopilarán datos a traves de cookies

# Paquete necesario (Usando un entorno virtual)

```
python3 -m venv venv
source venv/bin/activate
pip install yt_dlp
```

# Instalar ffmpeg para poder descargar los videos con una resolución alta

**NOTA:** Si usais `script_sin_ffmepg.py` es posible que obtengais el video en una resolución demasiado baja. Es aconsejable descargar ffmpeg para poder utilizar `script_con_ffmepg.py`.

**NOTA2:** Es posible que el video resultante de usar `script_con_ffmepg.py` no funcione si se usa VLC. En este caso, probad a cambiar de reproductor.

```
sudo apt install ffmpeg
```

# Enlaces de prueba


## Video de prueba del canal LG Chile 

https://www.youtube.com/watch?v=YCVnX0C7xuM


## Video de prueba del Canal Asmr Prog (Útil si vas a descargar tutoriales de programación)

https://www.youtube.com/watch?v=Nk0kiq-hss0
