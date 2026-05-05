'''Has un programa que: 
1- Pide un input de cualquier tipo al usuario
2- Invierta lo que digite el usuario
3- Muestra el resultado'''


print(" ")
print("*Programa para invertir inputs*")

while True:
    print("-" * 60)
    input_usuario = input("Digite lo que desea invertir o (fin) para salir: ").strip()

    if not input_usuario:
        print("Error: Digite algun valor de cualquier tipo.\n")
        continue
    elif input_usuario.lower() == "fin":
        print("\nSaliendo...\n")
        break
    else:
        invertido = input_usuario[::-1]
        print(f"Invertido = {invertido}\n")