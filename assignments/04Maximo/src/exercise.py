def main():
    #escribe tu código abajo de esta línea
    print("NUMERO MAYOOR")
    num1 = int(input("DAME EL NUMERO 1: "))
    num2 = int(input("DAME EL NUMERO 2: "))
    num3 = int(input("DAME EL NUMERO 3: "))


    if num1 > num2:
        print(num1) 
        if num2 > num3:
            print (num2)
        else:
             print(num3)

             if num1 > num3:
                print(num1)
             else:
                print(num3)      
    else:
     print(num2) 

    pass


if __name__ == '__main__':
    main()
