import os

# Exceção personalizada
class ProductNotFoundError(Exception):
    def __init__(self, product_name):
        super().__init__(f"Erro: Produto '{product_name}' não foi encontrado no inventário.")
        self.product_name = product_name

"""Esta e a classe 'pai' das classes eletonico e comida, e aonde fica armazenada informacoes gerais que ambas as duas prescisam."""
# Classes de produtos
class Produto:
    def __init__(self, id, nome, preco):
        self._id = id
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return f"{self._id} | {self._nome} | R${self._preco:.2f}"

    def get_nome(self):
        return self._nome

    def get_id(self):
        return self._id


class Eletronico(Produto):
    def __init__(self, id, nome, preco, garantia=9):
        super().__init__(id, nome, preco)
        self._garantia_meses = garantia

    def __str__(self):
        return f"{self._id} | {self._nome} | R${self._preco:.2f} | Garantia: {self._garantia_meses} meses"


class Comida(Produto):
    def __init__(self, id, nome, preco, validade):
        super().__init__(id, nome, preco)
        self._validade = validade

    def __str__(self):
        return f"{self._id} | {self._nome} | R${self._preco:.2f} | Validade: {self._validade}"

"""Esta e a classe inventario, e aonde fica armazenado todos os registros, de produtos que foram feitos """
# Classe Inventário
class Inventario:
    def __init__(self):
        self.__produtos = []
        self.__contador_id = 1  # contador para gerar IDs únicos

    def gerar_id(self):
        id_atual = self.__contador_id
        self.__contador_id += 1
        return id_atual

    def add_product(self, produto):
        self.__produtos.append(produto)

    def remove_product(self, product_name):
        for produto in self.__produtos:
            if produto.get_nome().lower() == product_name.lower():
                self.__produtos.remove(produto)
                print(f"--- Produto '{product_name}' removido com sucesso. ---")
                return
        raise ProductNotFoundError(product_name)

    def list_products(self):
        print("=== Sistema de Inventário ===")
        if not self.__produtos:
            print("--- Inventário vazio. ---")
        else:
            print("--- Produtos no inventário ---")
            for produto in self.__produtos:
                print(produto)

    def get_product(self, product_name):
        for produto in self.__produtos:
            if produto.get_nome().lower() == product_name.lower():
                return produto
        raise ProductNotFoundError(product_name)


""" esta parte do codigo e o menu inicial, sera o que o cliente vai visualizar quando rodar o codigo  """
def menu():
    inventario = Inventario()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Sistema de Inventário ===")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Listar produtos")
        print("4 - Sair")
        print("-----------------------------")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Adicionar Produto ===")
            tipo = input("Tipo de produto (eletronico/comida): ").strip().lower()
            nome = input("Nome do produto: ").strip()
            try:
                preco = float(input("Preço do produto: "))
            except ValueError:
                print("Erro: Preço inválido. Tente novamente.")
                input("Pressione Enter para continuar...")
                continue

            id_produto = inventario.gerar_id()

            if tipo == "eletronico":
                try:
                    garantia = int(input("Garantia (meses): "))
                except ValueError:
                    garantia = 9
                produto = Eletronico(id_produto, nome, preco, garantia)
            elif tipo == "comida":
                validade = input("Data de validade (ex: 20/08/2025): ").strip()
                produto = Comida(id_produto, nome, preco, validade)
            else:
                print("Erro: Tipo de produto inválido.")
                input("Pressione Enter para continuar...")
                continue

            inventario.add_product(produto)
            print(f"--- Produto '{nome}' adicionado com sucesso! ---")
            input("Pressione Enter para continuar...")

        elif escolha == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Remover Produto ===")
            nome = input("Nome do produto a remover: ").strip()
            try:
                inventario.remove_product(nome)
            except ProductNotFoundError as e:
                print(e)
            input("Pressione Enter para continuar...")

        elif escolha == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            inventario.list_products()
            print("-----------------------------")
            input("Pressione Enter para continuar...")

        elif escolha == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Sistema de Inventário ===")
            print("--- Obrigado por usar o sistema FastStock, quando puder deixe sua avaliacao no GitHub. Até mais! 🙋🏼‍♂️✌🏼  ---")
            break

        else:
            print("Erro: Opção inválida.")
            input("Pressione Enter para continuar...")


"""Volta ao menu """
menu()



