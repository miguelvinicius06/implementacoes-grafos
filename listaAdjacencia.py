#Lista de Adjacência
def criar_grafo():

    return {}


def inserir_vertice(grafo, vertice):

    if vertice not in grafo:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, nao_direcionado=False):

    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)

    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)

def vizinhos(grafo, vertice):

    if vertice in grafo:
        return grafo[vertice]
    return []

def listar_vizinhos(grafo, vertice):

    if vertice in grafo:
        lista = vizinhos(grafo, vertice)
        print(f"Vizinhos de {vertice}: {lista}")
        return lista
    else:
        print(f"O vértice {vertice} não existe no grafo.")
        return []

def exibir_grafo(grafo):

    print("\n--- Representação do Grafo (Lista de Adjacência) ---")
    if not grafo:
        print("O grafo está vazio.")
        return
    for vertice in sorted(grafo.keys(), key=str):
        print(f"{vertice} -> {grafo[vertice]}")
    print("--------------------------------------------------")

def remover_aresta(grafo, origem, destino, nao_direcionado=False):

    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)

    if nao_direcionado:
        if destino in grafo and origem in grafo[destino]:
            grafo[destino].remove(origem)


def remover_vertice(grafo, vertice, nao_direcionado=True):

    if vertice not in grafo:
        print(f"O vértice {vertice} não existe no grafo.")
        return False


    for outro in grafo:
        if vertice in grafo[outro]:
            grafo[outro].remove(vertice)


    del grafo[vertice]
    print(f"Vértice {vertice} removido com sucesso.")
    return True


def existe_aresta(grafo, origem, destino):

    if origem in grafo:
        return destino in grafo[origem]
    return False

def grau_vertices(grafo):

    graus = {}
    for v in grafo:
        graus[v] = {'out': 0, 'in': 0, 'total': 0}

    for u in grafo:
        graus[u]['out'] = len(grafo[u])
        for v in grafo[u]:
            if v in graus:
                graus[v]['in'] += 1

    for v in grafo:
        graus[v]['total'] = graus[v]['out'] + graus[v]['in']

    return graus


def percurso_valido(grafo, caminho):

    if not caminho or len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i+1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True


def main():

    grafo = criar_grafo()

    print("=== Configuração Inicial do Grafo ===")
    tipo_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
    nao_direcionado = tipo_input == 's'

    while True:
        print("\n================ MENU PRINCIPAL ================")
        print("1 - Exibir Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos de um Vértice")
        print("7 - Verificar se existe Aresta")
        print("8 - Calcular e Exibir Graus dos Vértices")
        print("9 - Verificar Percurso Válido")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            exibir_grafo(grafo)

        elif opcao == '2':
            v = input("Digite o nome do vértice a inserir: ").strip()
            if v:
                inserir_vertice(grafo, v)
                print(f"Vértice '{v}' inserido com sucesso.")
            else:
                print("Nome de vértice inválido.")

        elif opcao == '3':
            origem = input("Digite o vértice de origem: ").strip()
            destino = input("Digite o vértice de destino: ").strip()
            if origem and destino:
                inserir_aresta(grafo, origem, destino, nao_direcionado)
                print(f"Aresta entre '{origem}' e '{destino}' inserida com sucesso.")
            else:
                print("Vértices inválidos.")

        elif opcao == '4':
            v = input("Digite o vértice a remover: ").strip()
            if v:
                remover_vertice(grafo, v, nao_direcionado)
            else:
                print("Vértice inválido.")

        elif opcao == '5':
            origem = input("Digite o vértice de origem da aresta: ").strip()
            destino = input("Digite o vértice de destino da aresta: ").strip()
            if origem and destino:
                remover_aresta(grafo, origem, destino, nao_direcionado)
                print(f"Aresta entre '{origem}' e '{destino}' removida (se existia).")
            else:
                print("Vértices inválidos.")

        elif opcao == '6':
            v = input("Digite o vértice para listar vizinhos: ").strip()
            listar_vizinhos(grafo, v)

        elif opcao == '7':
            origem = input("Digite a origem: ").strip()
            destino = input("Digite o destino: ").strip()
            existe = existe_aresta(grafo, origem, destino)
            if existe:
                print(f"Sim! Existe aresta de '{origem}' para '{destino}'.")
            else:
                print(f"Não existe aresta direta de '{origem}' para '{destino}'.")

        elif opcao == '8':
            graus = grau_vertices(grafo)
            print("\n--- Graus dos Vértices ---")
            for v, g in graus.items():
                print(f"Vértice {v} -> Grau de Entrada: {g['in']}, Grau de Saída: {g['out']}, Grau Total: {g['total']}")
            print("--------------------------")

        elif opcao == '9':
            sequencia = input("Digite o percurso separado por vírgulas ou espaços (ex: A,B,C): ").strip()
            if ',' in sequencia:
                caminho = [s.strip() for s in sequencia.split(',') if s.strip()]
            else:
                caminho = [s.strip() for s in sequencia.split() if s.strip()]

            valido = percurso_valido(grafo, caminho)
            if valido:
                print(f"O percurso {caminho} é VÁLIDO!")
            else:
                print(f"O percurso {caminho} NÃO é válido.")

        elif opcao == '0':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()