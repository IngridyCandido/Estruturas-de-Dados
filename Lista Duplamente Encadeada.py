class No:

    def __init__(self, dado):
        self.dado = dado

        self.proximo = None
        self.anterior = None
class ListaDuplamenteEncadeada:

    def __init__(self):
        self.head = None
        self.tail = None

    def inserir(self, dado):
        novo = No(dado)
        if self.head is None:
            self.head = novo
            self.tail = novo
        else:
            self.tail.proximo = novo
            novo.anterior = self.tail
            self.tail = novo

    def inserir_antes(self, referencia, dado):
        atual = self.head

        while atual is not None:
            if atual.dado == referencia:
                novo = No(dado)

                # Liga o novo nó ao atual
                novo.proximo = atual
                novo.anterior = atual.anterior

                # Se não for o primeiro elemento
                if atual.anterior is not None:
                    atual.anterior.proximo = novo
                else:
                    # O atual era a cabeça
                    self.head = novo

                # Atualiza o ponteiro anterior do atual
                atual.anterior = novo

                return True

            atual = atual.proximo

        return False  # referência não encontrada

    def exibir(self):
        atual = self.head
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.proximo
        print()

    def exibir_reverso(self):
        atual = self.tail
        while atual is not None:
            print(atual.dado, end=" ")
            atual = atual.anterior
        print()

    def buscar(self, valor):
        atual = self.head
        while atual is not None:
            if atual.dado == valor:
                return True
            atual = atual.proximo
        return False

    def remover(self, valor):
        atual = self.head
        while atual is not None:
            if atual.dado == valor:
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.head = atual.proximo
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.tail = atual.anterior
                return True
            atual = atual.proximo
        return False    

# Teste da lista duplamente encadeada

lista = ListaDuplamenteEncadeada()

lista.inserir(10)
lista.inserir(20)
lista.inserir(30)

lista.exibir()  

lista.inserir_antes(20, 15)
lista.exibir()  

lista.inserir_antes(10, 5)
lista.exibir()  

lista.exibir_reverso() 

lista.remover(15)
lista.exibir()  

print(lista.buscar(20))
print(lista.buscar(100))