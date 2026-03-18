import random

numeros = [95, 1, 500, 20, 330, 40, 10, 200, 300, 50]

print(numeros)

def insertion_sort(numeros):
    for i in range(1, len(numeros)):
        key = numeros[i]
        j = i - 1
        while j >= 0 and key < numeros[j]:
            numeros[j + 1] = numeros[j]
            j -= 1
        numeros[j + 1] = key
    return numeros

print(insertion_sort(numeros))

lista_aleatoria1 = random.sample(range(1000), 100)

print(lista_aleatoria1)

def insertion_sort(lista_aleatoria1):
    for i in range(1, len(lista_aleatoria1)):
        key = lista_aleatoria1[i]
        j = i - 1
        while j >= 0 and key < lista_aleatoria1[j]:
            lista_aleatoria1[j + 1] = lista_aleatoria1[j]
            j -= 1
        lista_aleatoria1[j + 1] = key
    return lista_aleatoria1

print(insertion_sort(lista_aleatoria1))

lista_aleatoria2 = random.sample(range(10000), 1000)

print(lista_aleatoria2)

def insertion_sort(lista_aleatoria2):
    for i in range(1, len(lista_aleatoria2)):
        key = lista_aleatoria2[i]
        j = i - 1
        while j >= 0 and key < lista_aleatoria2[j]:
            lista_aleatoria2[j + 1] = lista_aleatoria2[j]
            j -= 1
        lista_aleatoria2[j + 1] = key
    return lista_aleatoria2

print(insertion_sort(lista_aleatoria2))

lista_aleatoria3 = random.sample(range(1000000), 100000)

print(lista_aleatoria3)

def insertion_sort(lista_aleatoria3):
    for i in range(1, len(lista_aleatoria3)):
        key = lista_aleatoria3[i]
        j = i - 1
        while j >= 0 and key < lista_aleatoria3[j]:
            lista_aleatoria3[j + 1] = lista_aleatoria3[j]
            j -= 1
        lista_aleatoria3[j + 1] = key
    return lista_aleatoria3

print(insertion_sort(lista_aleatoria3))