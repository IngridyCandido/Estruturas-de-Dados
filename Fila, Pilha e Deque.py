from collections import deque 

print("Preciso imprimir alguns documentos urgentes, vou organizar a fila de impressão...")
#Fila de impressão em Python

class FilaDeImpressao:
    def __init__(self):
        self.itens = []

    # enqueue -> adicionar ao final
    def enqueue(self, item):
        self.itens.append(item)

    # dequeue -> remover do início
    def dequeue(self):
        if self.itens:
            return self.itens.pop(0)
        return "Fila vazia"

    # front / peek -> ver primeiro item sem remover
    def peek(self):
        if self.itens:
            return self.itens[0]
        return "Fila vazia"

    # is_empty -> verificar se está vazia
    def is_empty(self):
        return len(self.itens) == 0

    # size -> quantidade
    def size(self):
        return len(self.itens)

    def conteudo(self):
        return self.itens

#Adicionando documentos à fila de impressão
fila = FilaDeImpressao()
fila.enqueue("trabalho.pdf")
fila.enqueue("relatorio.docx")
fila.enqueue("documento_final.pdf")

arquivos_impressao = fila.conteudo()
print(f"Conteúdo da fila: {arquivos_impressao}, enviando para impressão {fila.peek()}...")

while fila.conteudo():
        #Imprimindo o primeiro documento da fila
        documento_impresso = fila.dequeue()
        print(f"\nDocumento impresso: {documento_impresso}")
        if fila.conteudo():
            #Resto da fila após impressão
            conteudo_restante = fila.conteudo()
            print(f"Conteúdo da fila após impressão: {conteudo_restante}, {fila.size()} arquivos restantes.")
        elif fila.is_empty():
            print("Todos os documentos foram impressos.")
            break
print("\nAgora que a fila está vazia, vou ajustar o volume do computador para ouvir música enquanto trabalho...")
#Pilha de volume

class Volume:
    def __init__(self):
        self.itens = []

    # push -> empilhar
    def push(self, valor):
        self.itens.append(valor)

    # pop -> remover topo
    def pop(self):
        if self.itens:
            return self.itens.pop()
        return "Pilha vazia"

    # peek ou top -> ver topo
    def top(self):
        if self.itens:
            return self.itens[-1]
        return "Pilha vazia"


#Aumentando o volume
volume = Volume()
volume.push(10)
volume.push(20)
volume.push(30)
volume.push(40)

print(f"Aumentando o volume: {volume.itens}")

volume_atual = volume.top()
print(f"Volume atual: {volume_atual}")
print("\nOpa, acho que está alto demais...")
#Diminuindo o volume
print("Diminuindo o volume...")
volume_novo = volume.pop()
print(f"Volume abaixado para: {volume.top()}")

#Deque de playlist de música

playlist = deque()
playlist.append("musica1.mp3")
playlist.append("musica2.mp3") # adiciona no final
playlist.append("musica3.mp3") # adiciona no final
playlist.appendleft("Favorita.mp3") # adiciona no início

print(f"\nPlaylist atual: {playlist}")
print("Vou tocar minha música favorita primeiro...")
tocando = playlist.popleft()         # toca a música favorita e remove do início
print("\nTocando agora:", tocando)

print("Próximas:", playlist)
print(f"\nNão gosto muito da {playlist[0]}... Vou avançar e tocar a última da playlist primeiro: {playlist.pop()}") # remove a última música da playlist

print(f"Agora só tem: {playlist}, vou deixar tocar na sequencia!") 