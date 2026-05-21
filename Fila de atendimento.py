class Cliente:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

# Adiciona a implementação da fila
class FilaClientes:
    def __init__(self):
        self.clientes = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_clientes(self):
        if not self.clientes:
            print("Nenhum cliente na fila.")
            return
        for c in self.clientes:
            print(f"Senha {c.senha} - {c.nome}")

    def chamar_cliente(self):
        if not self.clientes:
            print("Nenhum cliente na fila.")
            return None
        cliente = self.clientes.pop(0)  # remove o cliente de menor senha
        print(f"\nChamando cliente: {cliente.senha}.")
        return cliente

class Caixa:
    def __init__(self, numero):
        self.numero = numero
        self.fila = FilaClientes()

    def adicionar_cliente(self, cliente):
        self.fila.adicionar_cliente(cliente)

    def listar_clientes(self):
        self.fila.listar_clientes()

    def chamar_cliente(self):
        return self.fila.chamar_cliente()

# Exemplo de uso
caixa1 = Caixa(1)

print("Adicionando clientes à fila do caixa 1:")

cliente1 = Cliente("Jose", 1)
cliente2 = Cliente("Maria", 2)
cliente3 = Cliente("João", 3)

# usar a API do Caixa (encapsulada)
caixa1.adicionar_cliente(cliente1)
caixa1.adicionar_cliente(cliente2)
caixa1.adicionar_cliente(cliente3)

caixa1.listar_clientes()

print("\nIniciando o atendimento dos clientes do caixa 1:")

for _ in range(len(caixa1.fila.clientes)):
    # Chamar cliente com menor senha
    if caixa1.fila.clientes:
        cliente_atendido = caixa1.chamar_cliente()
        print(f"Cliente {cliente_atendido.senha} atendido.")
        print("\nClientes restantes na fila do caixa 1:")
        caixa1.listar_clientes()

