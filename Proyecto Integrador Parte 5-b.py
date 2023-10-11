from Proyecto_Integrador_Parte_5 import *

def main():
    x = ArchivoJuego("", 0, 0, "maps")
    x.selecciona_archivo()
    x.leer_archivo()
    x.main_loop()

if name == "main":
    main()
