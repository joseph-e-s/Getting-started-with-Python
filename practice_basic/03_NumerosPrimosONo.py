'''Haz un programa que:
1- Pida un número al usuario
2- Determine si es primo o no
3- Muestre el resultado
(Un número primo: Solo se dividen entre 1 y ellos mismos, su division es exacta no sobra nada)'''

print(" ")
print("*Programa para detectar numeros primos*")

while True:
    print("-" * 43)
    num_usuario = input("Ingrese el numero o (fin) para salir: ").strip()
    
    if not num_usuario:
        print("Error: solo se permiten numeros o 'fin'.\n")
        continue

    if num_usuario.lower() == "fin":
        print("\nSaliendo...\n")
        break

    try:
        num_usuario = int(num_usuario)
    except ValueError:
        print("Error: solo se permiten numeros o 'fin'.\n")
        continue

    if num_usuario <= 1:
        print(f"({num_usuario}) No es un numero primo\n") 
    else:
        primo = True
        
        for numero in range(2, num_usuario):
            if num_usuario % numero == 0:
                primo = False
                break
        
        if primo == True:
            print(f"({num_usuario}) Si es un numero primo\n") 
        else:
            print(f"({num_usuario}) No es un numero primo\n") 
    