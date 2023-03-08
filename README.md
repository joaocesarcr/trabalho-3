
## Membros do Grupo
- 304342 - João César de Paula Criscolo - turma B
- 304317 - João Pedro Porto Pires de Oliveira - turma B
- 262875 - Willian Roger Pramio - turma B


## Parametros utilizados:
Solução ótima encontrada: [4, 7, 5, 3, 1, 6, 8, 2]
- Número de gerações: 40
- Número de indivíduos: 10
- Participantes do torneio: 4
- Proababilidade de mutação: valor dinânico baseado na diversidade dos -indivíduos.
- Elitistmo: 2

## Como executar o algorítmo:
Foi criado um jupyter notebook chamado [eight_queens.ipynb](/eight_queens.ipynb). Neste arquivo se encontram as funções alteradas utilizadas para chegar na solução ótima.
 
## Valores iniciais de theta_0 e theta_1
- theta_0=-3.0
- theta_1=5.0

## Extras implementados
Foi criado um novo notebook ([eight_queens.pdf](/eight_queens.pdf))
 para o problema das rainhas, onde foram realizadas as seguintes adições:
- Crossover point: passa a ser aleatório
- Adição da medida de diversidade ao gráfico.
- Mutation rate dinâmico: o mutation rate passa a inversamente proporcional a diversidade da população atual.


