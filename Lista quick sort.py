def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivo = lista[len(lista) // 2]

    menores = [x for x in lista if x < pivo]
    iguais = [x for x in lista if x == pivo]
    maiores = [x for x in lista if x > pivo]

    return quick_sort(menores) + iguais + quick_sort(maiores)
# Teste

numeros = [8, 3, 1, 7, 0, 10, 2]
resultado = quick_sort(numeros)

print("Lista original:", numeros)
print("Lista ordenada:", resultado)

def particionar(lista, inicio, fim):
    pivo = lista[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if lista[j] <= pivo:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[fim] = lista[fim], lista[i + 1]
    return i + 1

def quick_sort(lista, inicio, fim):
    if inicio < fim:
        indice_pivo = particionar(lista, inicio, fim)
        quick_sort(lista, inicio, indice_pivo - 1)
        quick_sort(lista, indice_pivo + 1, fim)

numeros = [8, 3, 1, 7, 0, 10, 2]
quick_sort(numeros, 0, len(numeros) - 1)

print(numeros)