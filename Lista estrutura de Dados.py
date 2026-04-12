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
        min_idx = i
        
        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j
        
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
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
# MERGE SORT
# =========================
def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        merge_sort(esquerda)
        merge_sort(direita)

        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i += 1
            else:
                lista[k] = direita[j]
                j += 1
            k += 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i += 1
            k += 1

        while j < len(direita):
            lista[k] = direita[j]
            j += 1
            k += 1

    return lista


# =========================
# QUICK SORT
# =========================
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


# =========================
# GERAR LISTA
# =========================
def gerar_lista(tamanho):
    return [random.randint(0, 1000) for _ in range(tamanho)]


# =========================
# TESTAR TEMPO
# =========================
def medir_tempo(funcao, lista):
    inicio = time.time()
    funcao(lista.copy())
    fim = time.time()
    return fim - inicio


# =========================
# EXERCÍCIOS 1 A 10
# =========================

print("\n--- Ordenação com 100 elementos ---")
lista_100 = gerar_lista(100)

print("Insertion:", insertion_sort(lista_100.copy())[:10], "...")
print("Selection:", selection_sort(lista_100.copy())[:10], "...")
print("Bubble:", bubble_sort(lista_100.copy())[:10], "...")
print("Merge:", merge_sort(lista_100.copy())[:10], "...")
print("Quick:", quick_sort(lista_100.copy())[:10], "...")


print("\n--- Tempo com 1000 elementos ---")
lista_1000 = gerar_lista(1000)

print("Insertion:", medir_tempo(insertion_sort, lista_1000))
print("Selection:", medir_tempo(selection_sort, lista_1000))
print("Bubble:", medir_tempo(bubble_sort, lista_1000))
print("Merge:", medir_tempo(merge_sort, lista_1000))
print("Quick:", medir_tempo(quick_sort, lista_1000))


# =========================
# EXERCÍCIO 11 (RANKING)
# =========================

print("\n--- Ranking com 2000 elementos ---")
lista_2000 = gerar_lista(2000)

tempos = {
    "Insertion": medir_tempo(insertion_sort, lista_2000),
    "Selection": medir_tempo(selection_sort, lista_2000),
    "Bubble": medir_tempo(bubble_sort, lista_2000),
    "Merge": medir_tempo(merge_sort, lista_2000),
    "Quick": medir_tempo(quick_sort, lista_2000)
}

ranking = sorted(tempos.items(), key=lambda x: x[1])

for i, (nome, tempo) in enumerate(ranking, 1):
    print(f"{i}º lugar: {nome} → {tempo:.5f} segundos")