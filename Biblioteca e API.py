import sortinpy, random, time

lista = random.sample(range(1, 100), 10)

print("Lista original:", lista)

lista_copia = lista.copy()
cont = time.time()

lista_copia.sort()
cont2 = time.time()
cont3 = cont2 - cont

print("\nLista ordenada (Método sort):", lista_copia)
print("Tempo de execução (Método sort):", cont3)

cont_bubble = time.time()
bubble_list = sortinpy.bubble_sort(lista)
cont_bubble2 = time.time()
cont_bubble3 = cont_bubble2 - cont_bubble

print("\nLista ordenada (Bubble Sort):", bubble_list)
print("Tempo de execução (Bubble Sort):", cont_bubble3)

cont_insertion = time.time()
insertion_list = sortinpy.insertion_sort(lista)
cont_insertion2 = time.time()
cont_insertion3 = cont_insertion2 - cont_insertion

print("\nLista ordenada (Insertion Sort):", insertion_list)
print("Tempo de execução (Insertion Sort):", cont_insertion3)

cont_shell = time.time()
shell_list = sortinpy.shell_sort(lista)
cont_shell2 = time.time()
cont_shell3 = cont_shell2 - cont_shell

print("\nLista ordenada (Shell Sort):", shell_list)
print("Tempo de execução (Shell Sort):", cont_shell3)

cont_merge = time.time()
merge_list = sortinpy.merge_sort(lista)
cont_merge2 = time.time()
cont_merge3 = cont_merge2 - cont_merge

print("\nLista ordenada (Merge Sort):", merge_list)
print("Tempo de execução (Merge Sort):", cont_merge3)

cont_selection = time.time()
selection_list = sortinpy.selection_sort(lista)
cont_selection2 = time.time()
cont_selection3 = cont_selection2 - cont_selection

print("\nLista ordenada (Selection Sort):", selection_list)
print("Tempo de execução (Selection Sort):", cont_selection3)

cont_quick = time.time()
quick_list = sortinpy.quick_sort(lista)
cont_quick2 = time.time()
cont_quick3 = cont_quick2 - cont_quick

print("\nLista ordenada (Quick Sort):", quick_list)
print("Tempo de execução (Quick Sort):", cont_quick3)

#Comparando os tempos de execução
tempos = {
    "Método sort": cont3,
    "Bubble Sort": cont_bubble3,
    "Insertion Sort": cont_insertion3,
    "Shell Sort": cont_shell3,
    "Merge Sort": cont_merge3,
    "Selection Sort": cont_selection3,
    "Quick Sort": cont_quick3
}

ordenados = sorted(tempos.items(), key=lambda x: x[1])

print("\nRanking de desempenho:")
for nome, tempo in ordenados:
    print(f"{nome}: {tempo}")

print("\nMelhor algoritmo:", ordenados[0][0])

#O que é Timsort?
print("\nTimsort é um algoritmo de ordenação híbrido derivado do merge sort e do insertion sort, " \
"projetado para ser eficiente em uma ampla variedade de casos. Ele é o algoritmo de ordenação padrão em Python e " \
"é otimizado para lidar com dados parcialmente ordenados, o que o torna muito rápido em muitos cenários do mundo real.")

#Complexidade
print("\nSua complexidade de tempo no pior caso é O(n log n), e no melhor caso é O(n), tornando-o uma escolha sólida para a ordenação de grandes conjuntos de dados.")

#Características
print("\nDentre suas características, vale destacar sua estabilidade e eficiência em dados quase ordenados. " \
"Além disso, o Timsort é adaptativo, o que significa que ele pode ajustar sua estratégia de ordenação com base na estrutura dos dados, " \
"tornando-o uma escolha versátil para uma variedade de aplicações.")
