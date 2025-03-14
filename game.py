# Personagem: Classe Mãe
# Heroi: Controlada pelo Usuario
# Inimigo: Adversario do Usuario

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNivel: {self.get_nivel()}"

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade) -> None:
        super().__init__(nome, vida, nivel) 
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidades: {self.get_habilidade()}"

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo) -> None:
        super().__init__(nome, vida, nivel) 
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}"

class Jogo:
    """ Classe orquestradora do Jogo """

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Bola de fogo")
        self.inimigo = Inimigo(nome="Sipós venenosos", vida=80, nivel=4, tipo="planta")

    def iniciar_batalha(self):
        """ Fazer a gestão da batalha em turnos """
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(f"\n{self.heroi.exibir_detalhes()}")
            print(f"\n{self.inimigo.exibir_detalhes()}")
            
            input("Pressione enter para atacar...")
            escolha = input("Escolha (1 - Ataque normal) (2 - Ataque Especial): ")

# Criar instâncias do jogo e iniciar batalha

jogo = Jogo()
jogo.iniciar_batalha()






