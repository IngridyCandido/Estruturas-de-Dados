def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

# Teste
numeros = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numeros))

import random
import time

def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista

# Função para testar tempo
def testar_tempo(tamanho):
    lista = [random.randint(0, 1000) for _ in range(tamanho)]
    
    inicio = time.time()
    bubble_sort(lista)
    fim = time.time()
    
    print(f"Tamanho: {tamanho} → Tempo: {fim - inicio:.5f} segundos")

# Testes
testar_tempo(10)
testar_tempo(100)
testar_tempo(10000)