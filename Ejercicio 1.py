# Ejercicio 1

# Tipo de dato: string
valor_1 = "Hola Mundo"

# Tipo de dato: list
valor_2 = [1, 10, 100]

# Tipo de dato: int
valor_3 = -25

# Tipo de dato: float
valor_4 = 1.167

# Tipo de dato: list
valor_5 = ["Hola", "Mundo"]

# Tipo de dato: string
valor_6 = ' '

# Impresiones para verificar los tipos de datos
print(type(valor_1))
print(type(valor_2))
print(type(valor_3))
print(type(valor_4))
print(type(valor_5))
print(type(valor_6))


#Ejercicio 2

a = 10
b = -5
c = "Hola "
d = [1, 2, 3]

print(a * 5)        # 50
print(a - b)        # 15
print(c + "Mundo")  # "Hola Mundo"
print(c * 2)        # "Hola Hola "
print(d[-1])         # 3 (último elemento de la lista)
print(d[1:])         # [2, 3] (sublista desde el segundo elemento)
print(d + d)         # [1, 2, 3, 1, 2, 3] (concatenación de listas)

#Ejercicio 3

numero_1 = 9
numero_2 = 3
numero_3 = 6

media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)


#Ejercicio 4

nota_1 = 10
nota_2 = 7
nota_3 = 4

# Porcentajes
porcentaje_nota_1 = 0.15
porcentaje_nota_2 = 0.35
porcentaje_nota_3 = 0.50

# Cálculo de la nota final
nota_final = (nota_1 * porcentaje_nota_1) + (nota_2 * porcentaje_nota_2) + (nota_3 * porcentaje_nota_3)

print("La nota final es:", nota_final)

# Ejercicio 5

matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]

# Corregir las sumas incorrectas en cada fila
for fila in matriz:
    fila[-1] = sum(fila[:-1])

# Imprimir la matriz corregida
print("Ejercicio 5")
for fila in matriz:
    print(fila)


# Ejercicio 6

cadena_corrupta = "zeréP nauJ,01"

# Voltear la cadena utilizando slicing
cadena_correcta = cadena_corrupta[::-1]

# Separar el nombre y la nota
nombre, nota = cadena_correcta.split(',')

# Formatear la cadena
mensaje_formateado = f"{nombre} ha sacado un Nota de {nota}."

# Imprimir el mensaje formateado
print(mensaje_formateado)


#Ejercicios « Operadores y expresiones

# Ejercicio 1


# Leer dos números por teclado
numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))

# Determinar aspectos
son_iguales = numero_1 == numero_2
son_diferentes = numero_1 != numero_2
primero_mayor_que_segundo = numero_1 > numero_2
segundo_mayor_o_igual_que_primero = numero_2 >= numero_1

# Mostrar resultados
print("¿Los dos números son iguales?", son_iguales)
print("¿Los dos números son diferentes?", son_diferentes)
print("¿El primero es mayor que el segundo?", primero_mayor_que_segundo)
print("¿El segundo es mayor o igual que el primero?", segundo_mayor_o_igual_que_primero)


# Ejercicio 2

# Leer una cadena de texto
cadena_texto = input("Ingrese una cadena de texto: ")

# Determinar longitud de la cadena
longitud_valida = 3 <= len(cadena_texto) < 10

# Mostrar resultado
print("¿La longitud es mayor o igual a 3 y menor que 10?", longitud_valida)


# Ejercicio 3

# Guardar el valor en una variable
numero_magico = 12345679

# Leer el numero_usuario
numero_usuario = int(input("Ingrese un número entre 1 y 9: "))

# Operadores en asignación
numero_usuario *= 9
numero_magico *= numero_usuario

# Mostrar el valor final de numero_magico
print("El valor final del numero_magico es:", numero_magico)
