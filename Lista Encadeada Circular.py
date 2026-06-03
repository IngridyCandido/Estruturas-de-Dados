class No:

    def __init__(self, dado):
        self.dado = dado

        self.proximo = None

class ListaCircular:

    def __init__(self):
        self.head = None

    def inserir(self, dado):
        novo = No(dado)
        if self.head is None:
            self.head = novo
            novo.proximo = novo
            return
        atual = self.head
        while atual.proximo != self.head:
            atual = atual.proximo
        atual.proximo = novo
        novo.proximo = self.head
    
    def exibir(self):
        if self.head is None:
            print("Lista vazia")
            return
        atual = self.head
        while True:
            print(atual.dado, end=" ")
            atual = atual.proximo
            if atual == self.head:
                break
        print()
        
    def buscar(self, valor):

        if self.head is None:
            return False

        atual = self.head

        while True:

            if atual.dado == valor:
                return True

            atual = atual.proximo

            if atual == self.head:
                break

        return False
    
    def remover(self, valor):
        if self.head is None:
            return False

        atual = self.head
        anterior = None

        while True:

            if atual.dado == valor:

                if anterior is not None:
                    anterior.proximo = atual.proximo
                else:
                    # Remover o head
                    if atual.proximo == self.head:
                        self.head = None  # Lista fica vazia
                    else:
                        self.head = atual.proximo
                        # Atualizar o último nó para apontar para o novo head
                        ultimo = self.head
                        while ultimo.proximo != atual:
                            ultimo = ultimo.proximo
                        ultimo.proximo = self.head

                return True

            anterior = atual
            atual = atual.proximo

            if atual == self.head:
                break

        return False

lista = ListaCircular()

lista.inserir(10)
lista.inserir(20)
lista.inserir(30)
lista.inserir(40)

lista.exibir()

print(lista.buscar(30))
print(lista.buscar(100))

lista.remover(20)
lista.exibir()