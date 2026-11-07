#Lista de Arestas


def criar_grafo():

    vertices = []
    arestas = []
    return vertices, arestas


def inserir_vertice(vertices, vertice):

    if vertice not in vertices:
        vertices.append(vertice)


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):

    inserir_vertice(vertices, origem)
    inserir_vertice(vertices, destino)


    if [origem, destino] not in arestas:
        arestas.append([origem, destino])

    if nao_direcionado:
        if [destino, origem] not in arestas:
            arestas.append([destino, origem])


def remover_aresta(arestas, origem, destino, nao_direcionado=False):

    if [origem, destino] in arestas:
        arestas.remove([origem, destino])
        print(f"Aresta [{origem}, {destino}] removida.")
    else:
        print(f"Aresta [{origem}, {destino}] não encontrada.")

    if nao_direcionado:
        if [destino, origem] in arestas:
            arestas.remove([destino, origem])


def remover_vertice(vertices, arestas, vertice):

    if vertice in vertices:
        vertices.remove(vertice)


        for aresta in arestas[:]:
            if vertice in aresta:
                arestas.remove(aresta)

        print(f"Vértice '{vertice}' e suas arestas conexas foram removidos.")
    else:
        print(f"O vértice '{vertice}' não existe no grafo.")


def existe_aresta(arestas, origem, destino):

    for aresta in arestas:
        if aresta == [origem, destino]:
            return True
    return False


def vizinhos(vertices, arestas, vertice):

    lista_vizinhos = []
    for origem, destino in arestas:
        if origem == vertice:
            if destino not in lista_vizinhos:
                lista_vizinhos.append(destino)
    return lista_vizinhos


def grau_vertices(vertices, arestas, nao_direcionado=False):


    graus = {}


    for v in vertices:
        if nao_direcionado:
            graus[v] = 0
        else:
            graus[v] = {"saida": 0, "entrada": 0, "total": 0}

    for origem, destino in arestas:
        if nao_direcionado:
            if origem in graus:
                graus[origem] += 1
        else:
            if origem in graus:
                graus[origem]["saida"] += 1
            if destino in graus:
                graus[destino]["entrada"] += 1

    if not nao_direcionado:
        for v in vertices:
            graus[v]["total"] = graus[v]["saida"] + graus[v]["entrada"]

    return graus


def percurso_valido(arestas, caminho):

    if not caminho or len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        u = caminho[i]
        v = caminho[i+1]
        if not existe_aresta(arestas, u, v):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):

    if vertice in vertices:
        lista = vizinhos(vertices, arestas, vertice)
        print(f"Vizinhos de '{vertice}': {lista}")
        return lista
    else:
        print(f"O vértice '{vertice}' não existe no grafo.")
        return []


def exibir_grafo(vertices, arestas):

    print("\n--- Representação do Grafo (Lista de Arestas) ---")
    print(f"Vértices: {vertices}")
    print("Arestas:")
    if not arestas:
        print("  (Nenhuma aresta cadastrada)")
    else:
        for origem, destino in arestas:
            print(f"  {origem} -> {destino}")
    print("-------------------------------------------------")


def main():
    vertices, arestas = criar_grafo()

    print("=== Configuração do Grafo (Lista de Arestas) ===")
    tipo = input("O grafo é não-direcionado? (s/n): ").strip().lower()
    nao_direcionado = tipo == 's'

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
            exibir_grafo(vertices, arestas)

        elif opcao == '2':
            v = input("Digite o nome do vértice: ").strip()
            if v:
                inserir_vertice(vertices, v)
                print(f"Vértice '{v}' inserido.")
            else:
                print("Nome inválido.")

        elif opcao == '3':
            origem = input("Vértice de origem: ").strip()
            destino = input("Vértice de destino: ").strip()
            if origem and destino:
                inserir_aresta(vertices, arestas, origem, destino, nao_direcionado)
                print(f"Aresta de '{origem}' para '{destino}' adicionada.")
            else:
                print("Vértices inválidos.")

        elif opcao == '4':
            v = input("Digite o vértice a remover: ").strip()
            remover_vertice(vertices, arestas, v)

        elif opcao == '5':
            origem = input("Origem da aresta: ").strip()
            destino = input("Destino da aresta: ").strip()
            remover_aresta(arestas, origem, destino, nao_direcionado)

        elif opcao == '6':
            v = input("Digite o vértice: ").strip()
            listar_vizinhos(vertices, arestas, v)

        elif opcao == '7':
            origem = input("Origem: ").strip()
            destino = input("Destino: ").strip()
            if existe_aresta(arestas, origem, destino):
                print(f"Sim, existe aresta de '{origem}' para '{destino}'.")
            else:
                print(f"Não existe aresta de '{origem}' para '{destino}'.")

        elif opcao == '8':
            graus = grau_vertices(vertices, arestas, nao_direcionado)
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

            if percurso_valido(arestas, caminho):
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