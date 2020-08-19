from typing import AnyStr

def NumeroPerfecto(numero : int):
    cont = 0
    cont2 = 0
    # Validar si es primo
    if numero < 9:
        print("el numero debe ser mayor a 9")
    else:
        if( es_primo(numero) == True):
            cont = contar_primos(numero)
            newNumber = str(numero)[::-1]
            # comparamos su espejo
            if( es_primo(int(newNumber))):
                cont2 = contar_primos(int(newNumber))
                if( str(cont) == str(cont2)[::-1]):
                    if(int(str(numero)[0]) * int(str(numero)[1]) == int(cont)):
                        binNumero = dec_to_bin(numero)
                        if( str(binNumero) == str(binNumero)[::-1]):#comparamos si es palindromo
                            print(f"el numero {numero} es un numero perfecto")
                        else:
                            print(f"el numero {numero} es binario no es palindromo")
                    else:
                        print(f"el numero {numero} separado y multiplado es {str(numero)[0]} x {str(numero)[1]} es difente de {cont}")
                else:
                    print(f"el numero {numero} es el {cont} primo y su espejo el {newNumber} es el {cont2} primo , tienen que ser iguales")
            else:
                print(f"el numero {numero} es primo , pero su espejo no lo es")
        else:
            print(f"el numero {numero} no es primo")
        



def es_primo(numero : int):
    if numero < 2:
        return False
    for num in range(2, numero):
        if numero % num == 0:
            return False
    return True

def contar_primos(numero : int) -> int:
    cont = 0
    for num in range(2, numero):
    # Contamos cuantos primos hay
        if es_primo(num) == True:
            cont += 1
    cont += 1
    return cont

def dec_to_bin(x):
    return int(bin(x)[2:])

numero = int(input("Ingrese su Numero : "))
NumeroPerfecto(numero)
