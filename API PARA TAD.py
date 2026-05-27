import queue
from collections import deque

pilha = deque()

pilha.append(10)
pilha.append(20)
pilha.append(30)

print(pilha)
elemento = pilha.pop()

print("Removido:", elemento)
print(pilha)

fila = deque()

fila.append("A")
fila.append("B")
fila.append("C")

print(fila)
removido = fila.popleft()

print("Removido:", removido)
print(fila)

fila = queue.Queue()

fila.put(1)
fila.put(2)
fila.put(3)

print(fila.get())
print(fila.get())

pilha = queue.LifoQueue()

pilha.put("A")
pilha.put("B")

print(pilha.get())