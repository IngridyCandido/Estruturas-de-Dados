class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

raiz = No(50)

raiz.esquerda = No(30)
raiz.direita = No(70)

raiz.esquerda.esquerda = No(20)
raiz.esquerda.direita = No(40)

raiz.direita.esquerda = No(60)
raiz.direita.direita = No(80)

#Imprimindo como uma arvore rotacionada

def imprime_arvore(no, nivel=0):
    if no is not None:
        imprime_arvore(no.direita, nivel + 1)
        print("    " * nivel + str(no.valor))
        imprime_arvore(no.esquerda, nivel + 1)

imprime_arvore(raiz)

#Imprimindo como uma arvore

def altura(no):
    if no is None:
        return 0
    return 1 + max(altura(no.esquerda), altura(no.direita))

def imprimir_arvore(raiz):
    if raiz is None:
        return

    h = altura(raiz)
    nivel_atual = [raiz]
    largura = 2 ** h

    for nivel in range(h):
        espacos = largura // (2 ** (nivel + 1))

        # Linha dos valores
        linha = ""
        proximos = []

        for no in nivel_atual:
            linha += " " * espacos

            if no:
                linha += str(no.valor)
                proximos.append(no.esquerda)
                proximos.append(no.direita)
            else:
                linha += " "
                proximos.extend([None, None])

            linha += " " * espacos

        print(linha)

        # Linha das conexões
        if nivel < h - 1:
            conexoes = ""
            for no in nivel_atual:
                conexoes += " " * (espacos - 1)

                if no and no.esquerda:
                    conexoes += "/"
                else:
                    conexoes += " "

                conexoes += " "

                if no and no.direita:
                    conexoes += "\\"
                else:
                    conexoes += " "

                conexoes += " " * (espacos - 1)

            print(conexoes)

        nivel_atual = proximos

print(imprimir_arvore(raiz))

#Imprimindo como uma arvore nível profissional

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


def altura(no):
    if no is None:
        return 0
    return 1 + max(altura(no.esquerda), altura(no.direita))


def imprimir_arvore2(raiz):
    h = altura(raiz)

    # largura suficiente para acomodar a árvore
    largura = (2 ** h) * 4
    altura_matriz = h * 2

    matriz = [[" " for _ in range(largura)] for _ in range(altura_matriz)]

    def desenhar(no, linha, coluna, deslocamento):
        if no is None:
            return

        valor = str(no.valor)

        # escreve o valor do nó
        inicio = coluna - len(valor) // 2
        for i, c in enumerate(valor):
            if 0 <= inicio + i < largura:
                matriz[linha][inicio + i] = c

        if no.esquerda:
            matriz[linha + 1][coluna - deslocamento // 2] = "/"
            desenhar(
                no.esquerda,
                linha + 2,
                coluna - deslocamento,
                max(2, deslocamento // 2)
            )

        if no.direita:
            matriz[linha + 1][coluna + deslocamento // 2] = "\\"
            desenhar(
                no.direita,
                linha + 2,
                coluna + deslocamento,
                max(2, deslocamento // 2)
            )

    desenhar(
        raiz,
        0,
        largura // 2,
        largura // 4
    )

    for linha in matriz:
        print("".join(linha).rstrip())

print(imprimir_arvore2(raiz))