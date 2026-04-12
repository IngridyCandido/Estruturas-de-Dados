import random
import time

# =========================
# INSERTION SORT
# =========================
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        
        lista[j + 1] = chave
    return lista


# =========================
# SELECTION SORT
# =========================
def selection_sort(lista):
    n = len(lista)
    
    for i in range(n):
        menor = i
        
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        
        lista[i], lista[menor] = lista[menor], lista[i]
    
    return lista


# =========================
# BUBBLE SORT
# =========================
def bubble_sort(lista):
    n = len(lista)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


# =========================
# GERAR LISTA ALEATÓRIA
# =========================
def gerar_lista(tamanho):
    return [random.randint(0, 1000) for _ in range(tamanho)]


# =========================
# MEDIR TEMPO
# =========================
def medir_tempo(funcao, lista):
    inicio = time.time()
    funcao(lista.copy())
    fim = time.time()
    return fim - inicio


# =========================
# QUESTÕES 1, 3 e 5
# Ordenar 100 elementos
# =========================
print("=== ORDENAÇÃO COM 100 ELEMENTOS ===\n")

lista_100 = gerar_lista(100)

print("Insertion Sort:")
print(insertion_sort(lista_100.copy()), "\n")

print("Selection Sort:")
print(selection_sort(lista_100.copy()), "\n")

print("Bubble Sort:")
print(bubble_sort(lista_100.copy()), "\n")


# =========================
# QUESTÕES 2, 4 e 6
# Tempo com 1000 elementos
# =========================
print("=== TEMPO DE EXECUÇÃO (1000 ELEMENTOS) ===\n")

lista_1000 = gerar_lista(1000)

tempo_insertion = medir_tempo(insertion_sort, lista_1000)
tempo_selection = medir_tempo(selection_sort, lista_1000)
tempo_bubble = medir_tempo(bubble_sort, lista_1000)

print(f"Insertion Sort: {tempo_insertion:.5f} segundos")
print(f"Selection Sort: {tempo_selection:.5f} segundos")
print(f"Bubble Sort: {tempo_bubble:.5f} segundos")