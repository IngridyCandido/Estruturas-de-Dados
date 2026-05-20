class Jogo:
    def __init__(self, nome, genero, horas, status):
        self.nome = nome
        self.genero = genero
        self.horas = horas
        self.status = status

    def exibir(self):
        print(f"Nome: {self.nome}")
        print(f"Gênero: {self.genero}")
        print(f"Horas jogadas: {self.horas}")
        print(f"Status: {self.status}")
        print("-" * 30)


class BibliotecaJogos:
    STATUS_VALIDOS = ["jogando", "zerado", "pendente"]

    def __init__(self):
        self.jogos = []

    # Adicionar jogo
    def adicionar_jogo(self, nome, genero, horas, status):

        # Verifica nome repetido
        for jogo in self.jogos:
            if jogo.nome.lower() == nome.lower():
                print("Erro: jogo já cadastrado.")
                return

        # Verifica status válido
        if status not in self.STATUS_VALIDOS:
            print("Erro: status inválido.")
            return

        # Verifica horas negativas
        if horas < 0:
            print("Erro: horas não podem ser negativas.")
            return

        novo_jogo = Jogo(nome, genero, horas, status)
        self.jogos.append(novo_jogo)

        print("Jogo adicionado com sucesso!")

    # Remover jogo
    def remover_jogo(self, nome):

        for jogo in self.jogos:
            if jogo.nome.lower() == nome.lower():
                self.jogos.remove(jogo)
                print("Jogo removido.")
                return

        print("Erro: jogo não encontrado.")

    # Atualizar horas
    def atualizar_horas(self, nome, novas_horas):

        if novas_horas < 0:
            print("Erro: horas inválidas.")
            return

        for jogo in self.jogos:
            if jogo.nome.lower() == nome.lower():
                jogo.horas = novas_horas
                print("Horas atualizadas.")
                return

        print("Erro: jogo não encontrado.")

    # Alterar status
    def alterar_status(self, nome, novo_status):

        if novo_status not in self.STATUS_VALIDOS:
            print("Erro: status inválido.")
            return

        for jogo in self.jogos:
            if jogo.nome.lower() == nome.lower():
                jogo.status = novo_status
                print("Status atualizado.")
                return

        print("Erro: jogo não encontrado.")

    # Listar jogos
    def listar_jogos(self):

        if len(self.jogos) == 0:
            print("Biblioteca vazia.")
            return

        print("\n=== BIBLIOTECA DE JOGOS ===")

        for jogo in self.jogos:
            jogo.exibir()


# ---------------- TESTE ----------------

biblioteca = BibliotecaJogos()

biblioteca.adicionar_jogo(
    "Minecraft",
    "Sandbox",
    120,
    "jogando"
)

biblioteca.adicionar_jogo(
    "God of War",
    "Ação",
    45,
    "zerado"
)

biblioteca.listar_jogos()

biblioteca.atualizar_horas(
    "Minecraft",
    150
)

biblioteca.alterar_status(
    "Minecraft",
    "zerado"
)

biblioteca.listar_jogos()

biblioteca.remover_jogo(
    "God of War"
)

biblioteca.listar_jogos()