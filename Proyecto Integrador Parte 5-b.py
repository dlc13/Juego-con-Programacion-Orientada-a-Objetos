from Proyecto_Integrador_Parte_5 import ArchivoJuego

def main():
    x = ArchivoJuego("", 0, 0, "c:\Users\Notebook\Desktop\maps")
    x.selecciona_archivo()
    x.leer_archivo()
    x.main_loop()

if name == "main":
    main()