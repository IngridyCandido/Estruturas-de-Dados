import time, random

#implementando selection sort 
def selection_sort(lista):
    n = len(lista)

    for i in range(n):
        menor_indice = i

        for j in range(i + 1, n):
            if lista[j] < lista[menor_indice]:
                menor_indice = j

        # Troca
        lista[i], lista[menor_indice] = lista[menor_indice], lista[i]

    return lista

# Teste
cont=time.time()

lista = [64, 25, 12, 22, 11]

print(f"\nA lista ordenada por selection sort é: {selection_sort(lista)}")

cont2=time.time()

cont3=cont2-cont

print(f"Foi executado em {round(cont3, 4)} segundos.")

#implementando quick sort 

def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)
#teste
cont_quick_sort = time.time()
numeros = [8, 3, 1, 7, 0]
print(f"\nA lista ordenada por quick sort é: {quick_sort(numeros)}")

cont_quick_sort2 = time.time()

cont_quick_sort3 = cont_quick_sort2 - cont_quick_sort

print(f"Foi executado em {round(cont_quick_sort3, 4)} segundos.")

#comparando métodos
if cont_quick_sort3 < cont3:
    print("\nO quick sort foi mais rápido que o selection sort.")
else:
    print("\nO selection sort foi mais rápido que o quick sort.")

# Lista aleatória com 10 números
cont=time.time()

lista_aleatoria1 = random.sample(range(100), 10)

print("\nLista aleatória com 10 números:")
print(lista_aleatoria1)

print("\nLista aleatória com 10 números ordenada por selection sort:")
print(selection_sort(lista_aleatoria1.copy()))

cont2=time.time()

cont3=cont2-cont

print(f"\nFoi executado pelo selection sort em {round(cont3, 4)} segundos.")

tempo_quick_sort = time.time()

numeros_aleatoria1 = random.sample(range(100), 10)

print("\nLista aleatória com 10 números:")
print(numeros_aleatoria1)

print("\nLista aleatória com 10 números ordenada por quick sort:")
print(quick_sort(numeros_aleatoria1.copy()))

tempo_quick_sort2=time.time()

tempo_quick_sort3=tempo_quick_sort2-tempo_quick_sort

print(f"\nFoi executado pelo quick sort em {round(tempo_quick_sort3, 4)} segundos.")

if tempo_quick_sort3 < cont3:
    print("\nO quick sort foi mais rápido que o selection sort na lista com 10 números.")
else:
    print("\nO selection sort foi mais rápido que o quick sort na lista com 10 números.")

# Lista aleatória com 1000 números
cont_selection_sort = time.time()

lista_aleatoria1 = random.sample(range(2000), 1000)

print("\nLista aleatória com 1000 números:")
print(lista_aleatoria1)

print("\nLista aleatória com 1000 números ordenada por selection sort:")
print(selection_sort(lista_aleatoria1.copy()))

cont_selection_sort2 = time.time()

cont_selection_sort3 = cont_selection_sort2 - cont_selection_sort

print(f"\nFoi executado pelo selection sort em {round(cont_selection_sort3, 4)} segundos.")

tempo_quick_sort = time.time()

numeros_aleatoria1 = random.sample(range(2000), 1000)

print("\nLista aleatória com 1000 números:")
print(numeros_aleatoria1)

print("\nLista aleatória com 1000 números ordenada por quick sort:")
print(quick_sort(numeros_aleatoria1.copy()))

tempo_quick_sort2=time.time()

tempo_quick_sort3=tempo_quick_sort2-tempo_quick_sort

print(f"\nFoi executado pelo quick sort em {round(tempo_quick_sort3, 4)} segundos.")

if tempo_quick_sort3 < cont_selection_sort3:
    print("\nO quick sort foi mais rápido que o selection sort na lista com 1000 números.")
else:
    print("\nO selection sort foi mais rápido que o quick sort na lista com 1000 números.")

# Lista aleatória com 1.000.000 números
cont_selection_sort = time.time()

lista_aleatoria1 = random.sample(range(2000000), 1000000)

print("\nLista aleatória com 1.000.000 números:")
print(lista_aleatoria1)

print("\nLista aleatória com 1.000.000 números ordenada por selection sort:")
print(selection_sort(lista_aleatoria1.copy()))

cont_selection_sort2 = time.time()

cont_selection_sort3 = cont_selection_sort2 - cont_selection_sort

print(f"\nFoi executado pelo selection sort em {round(cont_selection_sort3, 4)} segundos.")

tempo_quick_sort = time.time()

numeros_aleatoria1 = random.sample(range(2000000), 1000000)

print("\nLista aleatória com 1.000.000 números:")
print(numeros_aleatoria1)

print("\nLista aleatória com 1.000.000 números ordenada por quick sort:")
print(quick_sort(numeros_aleatoria1.copy()))

tempo_quick_sort2=time.time()

tempo_quick_sort3=tempo_quick_sort2-tempo_quick_sort

print(f"\nFoi executado pelo quick sort em {round(tempo_quick_sort3, 4)} segundos.")

if tempo_quick_sort3 < cont_selection_sort3:
    print("\nO quick sort foi mais rápido que o selection sort na lista com 1.000.000 números.")
else:
    print("\nO selection sort foi mais rápido que o quick sort na lista com 1.000.000 números.")
