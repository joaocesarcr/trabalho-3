import random
def evaluate(individual):
    """
    Recebe um indivíduo (lista de inteiros) e retorna o número de ataques
    entre rainhas na configuração especificada pelo indivíduo.
    Por exemplo, no individuo [2,2,4,8,1,6,3,4], o número de ataques é 10.

    :param individual:list
    :return:int numero de ataques entre rainhas no individuo recebido
    """
    atks = 0
    for i in range(len(individual)):
      lista = individual.copy()
      for j in range(len(lista)):
        if j == i:
          continue
        if individual[i] == lista[j] or (abs(individual[i] - lista[j]) == abs(i-j)):
          atks += 1
    return atks/2

def tournament(participants):
    """
    Recebe uma lista com vários indivíduos e retorna o melhor deles, com relação
    ao numero de conflitos
    :param participants:list - lista de individuos
    :return:list melhor individuo da lista recebida
    """
    best,best_index= float("inf"), 0

    for i,individual in enumerate(participants):
      value = evaluate(individual)
      if value < best:
        best = value
        best_index = i
    return participants[best_index]

def crossover(parent1, parent2, index):
    """
    Realiza o crossover de um ponto: recebe dois indivíduos e o ponto de
    cruzamento (indice) a partir do qual os genes serão trocados. Retorna os
    dois indivíduos com o material genético trocado.
    Por exemplo, a chamada: crossover([2,4,7,4,8,5,5,2], [3,2,7,5,2,4,1,1], 3)
    deve retornar [2,4,7,5,2,4,1,1], [3,2,7,4,8,5,5,2].
    A ordem dos dois indivíduos retornados não é importante
    (o retorno [3,2,7,4,8,5,5,2], [2,4,7,5,2,4,1,1] também está correto).
    :param parent1:list
    :param parent2:list
    :param index:int
    :return:list,list
    """
    return parent1[:index] + parent2[index:], parent2[:index] + parent1[index:]

def mutate(individual, m):
    """
    Recebe um indivíduo e a probabilidade de mutação (m).
    Caso random() < m, sorteia uma posição aleatória do indivíduo e
    coloca nela um número aleatório entre 1 e 8 (inclusive).
    :param individual:list
    :param m:int - probabilidade de mutacao
    :return:list - individuo apos mutacao (ou intacto, caso a prob. de mutacao nao seja satisfeita)
    """
    if random.random() <= m:
      new_pos = random.randint(0,7)
      new_n = random.randint(1,8)

      # para nao inserir o mesmo numero atual da posicao e falhar o teste:
      while new_n == individual[new_pos]:
        new_n = random.randint(1,8)

      individual[new_pos] = new_n
    return individual

def run_ga(g, n, k, m, e):
    """
    Executa o algoritmo genético e retorna o indivíduo com o menor número de ataques entre rainhas
    :param g:int - numero de gerações
    :param n:int - numero de individuos
    :param k:int - numero de participantes do torneio
    :param m:float - probabilidade de mutação (entre 0 e 1, inclusive)
    :param e:int - número de indivíduos no elitismo
    :return:list - melhor individuo encontrado
    """
    def select_parent(population):
      """
        Seleciona dois individuos de uma populacao
        :param population: lista com os individuos
        :return: 2 individuos (listas de 8 elementos)
      """
      p1 = random.choice(population)
      p2 = random.choice(population)
      return p1,p2


    numbers = range(1,9)
    participants = [random.choices(numbers,k=8) for _ in range(n)]

    # "Tradução" dos slides
    # https://docs.google.com/presentation/d/10iKeCsGLVC6qFJhJMD-qBNlNSKr5CyYjFzsrsnKLcYU/edit#slide=id.g1afaeddd4a2_0_136
    for _ in range(g):
      p = []
      while len(p) < e:
        p.append(tournament(random.sample(participants,k)))
        p1, p2 = select_parent(p)
        o1,o2 = crossover(p1,p2,3)
        o1 = mutate(o1,m); o2 = mutate(o2,m)
        p.append(o1);p.append(o2)

      participants += p

    #print(tournament(participants))
    #print(evaluate(tournament(participants)))
    return tournament(participants)


      


    raise NotImplementedError  # substituir pelo seu codigo
