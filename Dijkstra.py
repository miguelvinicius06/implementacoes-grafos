def criar_grafo():
    return {}


def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []


def inserir_aresta(grafo, origem, destino, peso, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    atualizado = False
    for i, (viz, _) in enumerate(grafo[origem]):
        if viz == destino:
            grafo[origem][i] = (destino, peso)
            atualizado = True
            break
    if not atualizado:
        grafo[origem].append((destino, peso))

    if nao_direcionado:
        atualizado_volta = False
        for i, (viz, _) in enumerate(grafo[destino]):
            if viz == origem:
                grafo[destino][i] = (origem, peso)
                atualizado_volta = True
                break
        if not atualizado_volta:
            grafo[destino].append((origem, peso))


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
    print("\n--- Representação do Grafo Ponderado (Lista de Adjacência) ---")
    if not grafo:
        print("O grafo está vazio.")
        return
    for vertice in sorted(grafo.keys(), key=str):
        itens = [f"{viz} (peso {peso})" for viz, peso in grafo[vertice]]
        print(f"{vertice} -> {itens}")
    print("-------------------------------------------------------------")


def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo:
        grafo[origem] = [(viz, peso) for viz, peso in grafo[origem] if viz != destino]

    if nao_direcionado and destino in grafo:
        grafo[destino] = [(viz, peso) for viz, peso in grafo[destino] if viz != origem]


def remover_vertice(grafo, vertice):
    if vertice not in grafo:
        print(f"O vértice {vertice} não existe no grafo.")
        return False

    for outro in grafo:
        grafo[outro] = [(viz, peso) for viz, peso in grafo[outro] if viz != vertice]

    del grafo[vertice]
    print(f"Vértice {vertice} removido com sucesso.")
    return True


def existe_aresta(grafo, origem, destino):
    if origem in grafo:
        return any(viz == destino for viz, _ in grafo[origem])
    return False


def grau_vertices(grafo, nao_direcionado=False):
    graus = {}
    for v in grafo:
        graus[v] = {'out': 0, 'in': 0, 'total': 0}

    for u in grafo:
        graus[u]['out'] = len(grafo[u])
        for v, _ in grafo[u]:
            if v in graus:
                graus[v]['in'] += 1

    for v in grafo:
        if nao_direcionado:
            graus[v]['total'] = graus[v]['out']
        else:
            graus[v]['total'] = graus[v]['out'] + graus[v]['in']

    return graus


def percurso_valido(grafo, caminho):
    if not caminho or len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True


def dijkstra(grafo, inicio, destino=None):
    if inicio not in grafo:
        return [], {}, {}, []

    infinito = float('inf')
    processados = []
    distancia = {v: infinito for v in grafo}
    anterior = {v: None for v in grafo}
    distancia[inicio] = 0

    while len(processados) < len(grafo):
        atual = None
        menor_dist = infinito

        for v in grafo:
            if v not in processados and distancia[v] < menor_dist:
                menor_dist = distancia[v]
                atual = v

        if atual is None or menor_dist == infinito:
            break

        if destino is not None and atual == destino:
            break

        for viz, peso in grafo[atual]:
            if viz not in processados:
                nova_dist = distancia[atual] + peso
                if nova_dist < distancia[viz]:
                    distancia[viz] = nova_dist
                    anterior[viz] = atual

        processados.append(atual)

    caminho = []
    if destino is not None and destino in grafo and distancia[destino] != infinito:
        passo = destino
        while passo is not None:
            caminho.append(passo)
            passo = anterior[passo]
        caminho.reverse()

    return caminho, distancia, anterior, processados


def main():
    grafo = criar_grafo()

    print("=== Configuração Inicial do Grafo Ponderado ===")
    tipo_input = input("O grafo é não-direcionado? (s/n): ").strip().lower()
    nao_direcionado = tipo_input == 's'

    while True:
        print("\n================ MENU PRINCIPAL ================")
        print("1 - Exibir Grafo")
        print("2 - Inserir Vértice")
        print("3 - Inserir Aresta Ponderada")
        print("4 - Remover Vértice")
        print("5 - Remover Aresta")
        print("6 - Listar Vizinhos de um Vértice")
        print("7 - Verificar se existe Aresta")
        print("8 - Calcular e Exibir Graus dos Vértices")
        print("9 - Verificar Percurso Válido")
        print("10 - Menor Caminho / Distâncias (Dijkstra)")
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
            peso_str = input("Digite o peso da aresta: ").strip().replace(',', '.')
            try:
                peso = float(peso_str)
                if peso.is_integer():
                    peso = int(peso)
                if origem and destino:
                    inserir_aresta(grafo, origem, destino, peso, nao_direcionado)
                    print(f"Aresta '{origem}' -> '{destino}' (peso {peso}) inserida com sucesso.")
                else:
                    print("Vértices inválidos.")
            except ValueError:
                print("Peso inválido! Digite um número.")

        elif opcao == '4':
            v = input("Digite o vértice a remover: ").strip()
            if v:
                remover_vertice(grafo, v)
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
            destino = input("Digite a destino: ").strip()
            if existe_aresta(grafo, origem, destino):
                print(f"Sim! Existe aresta de '{origem}' para '{destino}'.")
            else:
                print(f"Não existe aresta direta de '{origem}' para '{destino}'.")

        elif opcao == '8':
            graus = grau_vertices(grafo, nao_direcionado)
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

            if percurso_valido(grafo, caminho):
                print(f"O percurso {caminho} é VÁLIDO!")
            else:
                print(f"O percurso {caminho} NÃO é válido.")

        elif opcao == '10':
            inicio = input("Digite o vértice inicial: ").strip()
            if inicio not in grafo:
                print(f"O vértice '{inicio}' não existe no grafo.")
            else:
                destino_input = input("Digite o vértice de destino (ou deixe em branco para ver todas as distâncias): ").strip()
                destino = destino_input if destino_input else None
                if destino is not None and destino not in grafo:
                    print(f"O vértice de destino '{destino}' não existe no grafo.")
                else:
                    caminho, distancia, anterior, processados = dijkstra(grafo, inicio, destino)
                    print(f"\nProcessados: {processados}")
                    print("--- Tabela de Distâncias e Anteriores ---")
                    for v in sorted(grafo.keys(), key=str):
                        dist_exib = "∞" if distancia[v] == float('inf') else distancia[v]
                        print(f"Vértice {v} -> Distância: {dist_exib} | Anterior: {anterior[v]}")
                    if destino is not None:
                        if caminho:
                            print(f"\nMenor caminho de '{inicio}' até '{destino}': {caminho} (custo total: {distancia[destino]})")
                        else:
                            print(f"\nNão existe caminho de '{inicio}' até '{destino}'.")
                    print("-----------------------------------------")

        elif opcao == '0':
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()