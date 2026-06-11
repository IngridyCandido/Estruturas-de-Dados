
# 1 e 2. Implementação dos exemplos dos slides
# Criando um dicionário
aluno = {
    "nome": "João",
    "idade": 18
}

# Acessando um valor
print("Nome:", aluno["nome"])

# Acessando com get()
print("Nome com get:", aluno.get("nome"))
print("Telefone com get:", aluno.get("telefone"))  # retorna None

# Adicionando elementos
aluno["curso"] = "Informática"
aluno["cidade"] = "Natal"

print("\nApós adicionar elementos:")
print(aluno)

# Alterando valor
aluno["idade"] = 19

print("\nApós alterar a idade:")
print(aluno)

# 3. Exibir todas as chaves

print("\nTodas as chaves:")
for chave in aluno.keys():
    print(chave)

# 4. Exibir todos os valores

print("\nTodos os valores:")
for valor in aluno.values():
    print(valor)

# 5. Verificar se uma chave existe

chave = "idade"

if chave in aluno:
    print(f"\nA chave '{chave}' existe.")
else:
    print(f"\nA chave '{chave}' não existe.")

# 6. Verificar se um valor existe

valor = "Informática"

if valor in aluno.values():
    print(f"O valor '{valor}' existe.")
else:
    print(f"O valor '{valor}' não existe.")

# Exemplo de remoção

del aluno["cidade"]

print("\nApós remover cidade:")
print(aluno)

# Limpar todo o dicionário
aluno.clear()

print("\nApós clear():")
print(aluno)