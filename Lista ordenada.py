import random

def insertion_sort(lista):
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1

        while j >= 0 and key < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = key

    return lista


# Lista inicial
numeros = [95, 1, 500, 20, 330, 40, 10, 200, 300, 50]

print("Lista original:")
print(numeros)

print("\nLista ordenada:")
print(insertion_sort(numeros.copy()))


# Lista aleatória 1 (100 números)
lista_aleatoria1 = random.sample(range(1000), 100)

print("\nLista aleatória 1:")
print(lista_aleatoria1)

print("\nLista aleatória 1 ordenada:")
print(insertion_sort(lista_aleatoria1.copy()))


# Lista aleatória 2 (1000 números)
lista_aleatoria2 = random.sample(range(10000), 1000)

print("\nLista aleatória 2:")
print(lista_aleatoria2)

print("\nLista aleatória 2 ordenada:")
print(insertion_sort(lista_aleatoria2.copy()))


# Lista aleatória 3 (100000 números)
lista_aleatoria3 = random.sample(range(1000000), 100000)

print("\nLista aleatória 3:")
print(lista_aleatoria3)

print("\nLista aleatória 3 ordenada:")
print(insertion_sort(lista_aleatoria3.copy()))