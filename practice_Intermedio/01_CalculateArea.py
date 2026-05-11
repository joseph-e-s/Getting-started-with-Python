'''
ÁREA DE UN POLÍGONO
Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
'''


def calcular_area(poligono, base=0, altura=0, lado=0):
    poligono = poligono.strip().lower()
    if poligono == 'cuadrado':
        return lado * lado
    if poligono == 'rectangulo':
        return base * altura
    if poligono == 'triangulo':
        return base * altura / 2
    return None


if __name__ == '__main__':
    print("Calculadora de áreas (tú introduces las medidas).")

    while True:
        print("\nPolígonos: 1) triángulo  2) cuadrado  3) rectángulo  (q) salir")
        opcion = input("Elige opción: ").strip().lower()
        if opcion in ('q', 'quit', 'salir'):
            print("Hasta luego.")
            break

        mapa = {'1': 'triangulo', '2': 'cuadrado', '3': 'rectangulo',
                'triangulo': 'triangulo', 'triángulo': 'triangulo',
                'cuadrado': 'cuadrado', 'rectangulo': 'rectangulo', 'rectángulo': 'rectangulo'}
        poligono = mapa.get(opcion)
        if poligono is None:
            print("Error: opción no reconocida. Usa 1, 2, 3 o el nombre del polígono.")
            continue

        base = altura = lado = 0.0

        try:
            if poligono == 'cuadrado':
                while True:
                    try:
                        t = input("Lado del cuadrado: ").strip().replace(',', '.')
                        lado = float(t)
                    except ValueError:
                        print("Error: introduce un número válido (ej. 5 o 3.5).")
                        continue
                    if lado <= 0:
                        print("Error: la medida debe ser mayor que cero.")
                        continue
                    break
            elif poligono == 'rectangulo':
                while True:
                    try:
                        t = input("Base del rectángulo: ").strip().replace(',', '.')
                        base = float(t)
                    except ValueError:
                        print("Error: introduce un número válido (ej. 5 o 3.5).")
                        continue
                    if base <= 0:
                        print("Error: la medida debe ser mayor que cero.")
                        continue
                    break
                while True:
                    try:
                        t = input("Altura del rectángulo: ").strip().replace(',', '.')
                        altura = float(t)
                    except ValueError:
                        print("Error: introduce un número válido (ej. 5 o 3.5).")
                        continue
                    if altura <= 0:
                        print("Error: la medida debe ser mayor que cero.")
                        continue
                    break
            else:
                while True:
                    try:
                        t = input("Base del triángulo: ").strip().replace(',', '.')
                        base = float(t)
                    except ValueError:
                        print("Error: introduce un número válido (ej. 5 o 3.5).")
                        continue
                    if base <= 0:
                        print("Error: la medida debe ser mayor que cero.")
                        continue
                    break
                while True:
                    try:
                        t = input("Altura del triángulo: ").strip().replace(',', '.')
                        altura = float(t)
                    except ValueError:
                        print("Error: introduce un número válido (ej. 5 o 3.5).")
                        continue
                    if altura <= 0:
                        print("Error: la medida debe ser mayor que cero.")
                        continue
                    break
        except (EOFError, KeyboardInterrupt):
            print("\nOperación cancelada.")
            break

        area = calcular_area(poligono, base=base, altura=altura, lado=lado)
        if area is None:
            print("Error: no se pudo calcular el área para ese polígono.")
        else:
            print(f"El área del {poligono} es: {area}")
