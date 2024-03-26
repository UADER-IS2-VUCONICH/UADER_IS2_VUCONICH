#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*
import sys

def factorial(num): 
    if num < 0: 
        print("Factorial de un número negativo no existe")
        return None

    elif num == 0: 
        return 1

    else: 
        fact = 1
        while(num > 1): 
            fact *= num 
            num -= 1
        return fact 

if len(sys.argv) < 2:
    print("Debe informar un número!")
    num = input("Ingrese un número para calcular el factorial: ")
    if not num.isdigit():
        print("Error: Debe ingresar un número entero.")
        sys.exit()
else:
    num = int(sys.argv[1])

print("Factorial", num, "! es", factorial(int(num)))

