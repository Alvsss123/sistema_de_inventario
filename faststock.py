import os
from datetime import datetime

# Exceção personalizada
class ProductNotFoundError(Exception):
    def __init__(self, product_id):
        super().__init__(f"Erro: Produto com ID '{product_id}' não foi encontrado no inventário.")
        self.product_id = product_id

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

# Classe Inventário
class Inventario:
    def __init__(self):
        self.__produtos = []
        self.__contador_id = 1

    def gerar_id(self):
        id_atual = self.__contador_id
        self.__contador_id += 1
        return id_atual

    def add_product(self, produto):
        self.__produtos.append(produto)

    def remove_product(self, product_id):
        for produto in self.__produtos:
            if produto.get_id() == product_id:
                self.__produtos.remove(produto)
                print(f"--- Produto com ID {product_id} removido com sucesso. ---")
                return
        raise ProductNotFoundError(product_id)

    def list_products(self):
        print("=== Sistema de Inventário ===")
        if not self.__produtos:
            print("--- Inventário vazio. ---")
        else:
            print("--- Produtos no inventário ---")
            for produto in self.__produtos:
                print(produto)

    def get_product(self, product_id):
        for produto in self.__produtos:
            if produto.get_id() == product_id:
                return produto
        raise ProductNotFoundError(product_id)

    def buscar_produto(self, termo):
        resultados = []
        try:
            termo_id = int(termo)
            for produto in self.__produtos:
                if produto.get_id() == termo_id:
                    resultados.append(produto)
        except ValueError:
            for produto in self.__produtos:
                if termo.lower() in produto.get_nome().lower():
                    resultados.append(produto)
        return resultados

# Menu principal
def menu():
    inventario = Inventario()

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== Sistema de Inventário ===")
        print("1 - Adicionar produto")
        print("2 - Remover produto")
        print("3 - Listar produtos")
        print("4 - Buscar produto")
        print("5 - Sair")
        print("-----------------------------")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Adicionar Produto ===")
            tipo = input("Tipo de produto (eletronico/comida): ").strip().lower()
            nome = input("Nome do produto: ").strip()
            try:
                preco = float(input("Preço do produto: "))
                if preco <= 0:
                    raise ValueError("Preço deve ser maior que zero.")
            except ValueError as e:
                print(f"Erro: {e}")
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
                try:
                    data_validade = datetime.strptime(validade, "%d/%m/%Y")
                    if data_validade <= datetime.now():
                        print("Erro: A data de validade deve ser no futuro.")
                        input("Pressione Enter para continuar...")
                        continue
                except ValueError:
                    print("Erro: Formato de data inválido. Use DD/MM/AAAA.")
                    input("Pressione Enter para continuar...")
                    continue
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
            try:
                product_id = int(input("ID do produto a remover: "))
                inventario.remove_product(product_id)
            except ValueError:
                print("Erro: ID inválido.")
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
            print("=== Buscar Produto ===")
            termo = input("Digite o nome ou ID do produto: ").strip()
            resultados = inventario.buscar_produto(termo)
            if resultados:
                print("--- Produtos encontrados ---")
                for produto in resultados:
                    print(produto)
            else:
                print("--- Nenhum produto encontrado. ---")
            input("Pressione Enter para continuar...")

        elif escolha == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== Sistema de Inventário ===")
            print("--- Obrigado por usar o sistema FastStock. Até mais! 🙋🏼‍♂️✌🏼---")
            break

        else:
            print("Erro: Opção inválida.")
            input("Pressione Enter para continuar...")

# Executa o menu
menu()






