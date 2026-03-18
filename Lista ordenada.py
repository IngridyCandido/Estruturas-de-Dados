numeros = [95, 1, 500, 20, 330, 40]

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