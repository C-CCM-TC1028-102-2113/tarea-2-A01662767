
def main():
    #escribe tu código abajo de esta línea
    print("LICENCIA")
    edad = int(input("DAME EL NUMERO: "))
    licencia = input("TIENES LICENCIA (S/N)?: ")
    


    if edad >= 18 and licencia == "S":
        print("TRAMITE LA LICENCIA")
    else:
        print("NO CUMPLES LO SOLICITADO")

   
   
    pass


if __name__ == '__main__':
    main()
