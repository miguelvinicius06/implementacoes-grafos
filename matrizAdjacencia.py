#Matriz de Adjacência

def criar_grafo():

    matriz = []
    vertices = []
    return matriz, vertices


def inserir_vertice(matriz, vertices, vertice):

    if vertice not in vertices:
        vertices.append(vertice)

        for linha in matriz:
            linha.append(0)

        nova_linha = [0] * len(vertices)
        matriz.append(nova_linha)


def inserir_aresta(matriz, vertices, origem, destino, nao_direcionado=False):

    if origem not in vertices:
        inserir_vertice(matriz, vertices, origem)
    if destino not in vertices:
        inserir_vertice(matriz, vertices, destino)

    i = vertices.index(origem)
    j = vertices.index(destino)

    matriz[i][j] = 1
    if nao_direcionado:
        matriz[j][i] = 1


def remover_vertice(matriz, vertices, vertice):

    if vertice in vertices:
        idx = vertices.index(vertice)

        matriz.pop(idx)

        for linha in matriz:
            linha.pop(idx)


        vertices.pop(idx)
        print(f"Vértice '{vertice}' removido com sucesso.")
    else:
        print(f"O vértice '{vertice}' não existe no grafo.")

def remover_aresta(matriz, vertices, origem, destino, nao_direcionado=False):

    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)

        matriz[i][j] = 0
        if nao_direcionado:
            matriz[j][i] = 0
        print(f"Aresta entre '{origem}' e '{destino}' removida.")
    else:
        print("Um ou ambos os vértices não existem no grafo.")


def existe_aresta(matriz, vertices, origem, destino):

    if origem in vertices and destino in vertices:
        i = vertices.index(origem)
        j = vertices.index(destino)
        return matriz[i][j] == 1
    return False


def vizinhos(matriz, vertices, vertice):

    lista_vizinhos = []
    if vertice in vertices:
        i = vertices.index(vertice)
        for j in range(len(vertices)):
            if matriz[i][j] == 1:
                lista_vizinhos.append(vertices[j])
    return lista_vizinhos


def grau_vertices(matriz, vertices, nao_direcionado=False):

    graus = {}
    n = len(vertices)

    for i in range(n):
        v = vertices[i]
        saida = sum(matriz[i])

        entrada = sum(matriz[row][i] for row in range(n))

        if nao_direcionado:

            graus[v] = saida
        else:
            graus[v] = {"saida": saida, "entrada": entrada, "total": saida + entrada}

    return graus


def percurso_valido(matriz, vertices, caminho):

    if not caminho or len(caminho) < 2:
        return True

    for k in range(len(caminho) - 1):
        u = caminho[k]
        v = caminho[k+1]
        if not existe_aresta(matriz, vertices, u, v):
            return False
    return True


def listar_vizinhos(matriz, vertices, vertice):

    if vertice in vertices:
        lista = vizinhos(matriz, vertices, vertice)
        print(f"Vizinhos de {vertice}: {lista}")
        return lista
    else:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return []


def exibir_grafo(matriz, vertices):

    print("\n--- Matriz de Adjacência ---")
    if not vertices:
        print("O grafo está vazio.")
        return


    cabecalho = "     " + "  ".join(str(v) for v in vertices)
    print(cabecalho)


    for i in range(len(vertices)):
        linha_str = "  ".join(str(val) for val in matriz[i])
        print(f"{vertices[i]} [ {linha_str} ]")
    print("-----------------------------")


def main():
    matriz, vertices = criar_grafo()

    print("=== Configuração do Grafo (Matriz) ===")
    tipo = input("O grafo é não-direcionado? (s/n): ").strip().lower()
    nao_direcionado = tipo == 's'

    while True:
        print("\n================ MENU PRINCIPAL ================")
        print("1 - Exibir Grafo (Matriz)")
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
            exibir_grafo(matriz, vertices)

        elif opcao == '2':
            v = input("Digite o nome do vértice: ").strip()
            if v:
                inserir_vertice(matriz, vertices, v)
                print(f"Vértice '{v}' inserido.")
            else:
                print("Nome inválido.")

        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            if origem and destino:
                inserir_aresta(matriz, vertices, origem, destino, nao_direcionado)
                print(f"Aresta de '{origem}' para '{destino}' adicionada.")
            else:
                print("Vértices inválidos.")

        elif opcao == '4':
            v = input("Digite o vértice a remover: ").strip()
            remover_vertice(matriz, vertices, v)

        elif opcao == '5':
            origem = input("Origem da aresta: ").strip()
            destino = input("Destino da aresta: ").strip()
            remover_aresta(matriz, vertices, origem, destino, nao_direcionado)

        elif opcao == '6':
            v = input("Digite o vértice: ").strip()
            listar_vizinhos(matriz, vertices, v)

        elif opcao == '7':
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if existe_aresta(matriz, vertices, origem, destino):
                print(f"Sim, existe aresta direta de '{origem}' para '{destino}'.")
            else:
                print(f"Não existe aresta direta de '{origem}' para '{destino}'.")

        elif opcao == '8':
            graus = grau_vertices(matriz, vertices, nao_direcionado)
            print("\n--- Graus dos Vértices ---")
            for v, g in graus.items():
                if nao_direcionado:
                    print(f"Vértice {v} -> Grau: {g}")
                else:
                    print(f"Vértice {v} -> Saída: {g['saida']}, Entrada: {g['entrada']}, Total: {g['total']}")
            print("--------------------------")

        elif opcao == '9':
            sequencia = input("Digite o percurso separado por vírgula ou espaço (ex: A,B,C): ").strip()
            if ',' in sequencia:
                caminho = [s.strip() for s in sequencia.split(',') if s.strip()]
            else:
                caminho = [s.strip() for s in sequencia.split() if s.strip()]

            if percurso_valido(matriz, vertices, caminho):
                print(f"O percurso {caminho} é VÁLIDO!")
            else:
                print(f"O percurso {caminho} NÃO é válido.")

        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()