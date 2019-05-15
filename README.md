# Repositorio charla de intro a embebidos

Este repositorio consiste en todo lo que se hablara en el modulo de "Introduccion a Raspberry PI",
recuerden que cualquier cosa pueden enviarme informacion a felipe.molina@wisely.cl

## Conectandote a Raspberry PI (Windows)
**Se require un cable de red y un notebook conectado a wifi. Ademas de windows actualizado**

- Primero, debemos configurar nuestra conexion wifi para habilitar compartir internet (share internet connection)
- Entrar a la consola (boton de windows + cmd)
- escribir ipconfig y anotar la IP que exista en nuestra IP ethernet (por ejemplo, 192.168.137.1) 
- Realizar un ping a la direccion IP ethernet broadcast (192.168.137.255)
- Revisar la tabla de direcciones arp -a y anotar la IP que este en nuestra red ethernet local (192.168.137.68, por ejemplo)
- conectar por ssh a la raspberry (ssh pi@192.168.137.68)
- las credencial por defecto es raspberry
- celebrar

## Activando escritorio remoto
- Entre por ssh a su raspberry PI
- ejecute el comando `sudo apt-get install tightvncserver`
- iniciar el escritorio remoto, en la terminal escribir `vncserver:1`
- La primera vez, te pediran escribir un password de 8 digitos, ingresa el que mas te guste (que probablemente sea 12345678...)
- En Windows, instalar VNC Client
- Ejecutar, y crear un nuevo usuario con la IP de la raspsberry mas el puerto 1 (por ejemplo, 192.168.137.68:1)
- Ingresar, colocar nuestra key y listo!

## Activando GPIOs
- entrar a la carpeta controladora (en la terminal de raspberry, escribir `cd /sys/class/gpio`)
- revisar wiring pi! https://pinout.xyz/pinout/wiringpi
- activar el PIN (`echo 4 > export`)
- entrar a la carpeta del gpio4
- cambiar direccion (`echo out > direction`) y activar pin ('echo 1 > value`)
- Maravillarse de la electronica moderna

## A traves de python
- entrar a python en la raspberry (`python3` en la terminal)
- activar la libreria (`import RPi.GPIO as io`)
- configurar parametros (`io.setmode(io.BOARD)`)
- configurar canal `io.setup(CHANNEL, io.OUT)`
- encender canal! `io.output(CHANNEL, True)`

## Ejecutar servidor web de ejemplo
- en la carpeta, crear un ambiente virtual (python3 -m venv venv)
- acceder a nuestro ambiente virtual (`source venv/bin/activate`)
- instalar las librerias de python (`pip install flask RPi.GPIO`)
- ejecutar python app.py
- entrar a la pagina web! (recuerda usar la direccion IP de la raspberry)

