#Exercício 1 – Criação de Dicionários

aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Sistemas de Informação"
}
print(aluno)

#Exercício 2 – Acesso aos Elementos

carro = {
    "marca": "Hyundai",
    "modelo": "HB20",
    "ano": 2022
}
print(carro["marca"])
print(carro["ano"])

#Exercício 3 – Alteração de Valores

produto = {
    "nome": "Mouse",
    "preco": 50
}

produto["preco"] = 65
print(produto)

#Exercício 4 – Inserção de Novos Elementos

livro = {
    "titulo": "Python Básico",
    "autor": "Ana Silva"
}

livro["ano"] = 2025
print(livro)

#Exercício 5 – Remoção de Elementos

pessoa = {
    "nome": "Maria",
    "idade": 30,
    "cidade": "Natal"
}

del pessoa["cidade"]
print(pessoa)

#Exercício 6 – Percorrendo um Dicionário

aluno = {
    "nome": "Pedro",
    "idade": 18,
    "curso": "Engenharia de Software"
}

for chave, valor in aluno.items():
    print(chave, ":", valor)

#Exercício 7 – Verificação de Chaves

contato = {
    "nome": "Carlos",
    "telefone": "99999-9999"
}

if "email" in contato:
    print(contato["email"])
else:
    print("Email não cadastrado.")

#Exercício 8 – Média das Notas

notas = {
    "Matemática": 8.5,
    "Português": 7.0,
    "História": 9.0
}

media = sum(notas.values()) / len(notas)
print(media)

#Exercício 9 – Frequência de Palavras
def exercicio9():
    frase = input("Digite uma frase: ")

    palavras = frase.split()

    frequencia = {}

    for palavra in palavras:
        if palavra in frequencia:
            frequencia[palavra] += 1
        else:
            frequencia[palavra] = 1

    print("Exercício 9")
    print(frequencia)
    print()

#Exercício 10 – Cadastro de Alunos

def exercicio10():
    alunos = {}

    quantidade = int(input("Quantos alunos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\nAluno {i+1}")

        nome = input("Nome: ")
        idade = int(input("Idade: "))
        nota = float(input("Nota final: "))

        alunos[nome] = {
            "idade": idade,
            "nota": nota
        }

    print("\nAlunos cadastrados:")
    for nome, dados in alunos.items():
        print(nome, dados)

    melhor_aluno = max(alunos, key=lambda nome: alunos[nome]["nota"])

    media = sum(aluno["nota"] for aluno in alunos.values()) / len(alunos)

    print(f"\nAluno com maior nota: {melhor_aluno}")
    print(f"Média da turma: {media:.2f}")
    print()

#Exercício 11 – Sistema de Controle de Estoque

def exercicio11():
    estoque = {}

    quantidade = int(input("Quantos produtos deseja cadastrar? "))

    for i in range(quantidade):
        print(f"\nProduto {i+1}")

        nome = input("Nome do produto: ")
        qtd = int(input("Quantidade em estoque: "))
        preco = float(input("Preço unitário: "))

        estoque[nome] = {
            "quantidade": qtd,
            "preco": preco
        }

    print("\nProdutos cadastrados:")
    for produto, dados in estoque.items():
        print(produto, dados)

    valor_total = sum(
        dados["quantidade"] * dados["preco"]
        for dados in estoque.values()
    )

    produto_mais_caro = max(
        estoque,
        key=lambda produto: estoque[produto]["preco"]
    )

    print(f"\nValor total do estoque: R$ {valor_total:.2f}")
    print(f"Produto mais caro: {produto_mais_caro}")
    print()

exercicio9()
exercicio10()
exercicio11()