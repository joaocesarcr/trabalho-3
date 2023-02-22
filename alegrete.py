import numpy as np


def compute_mse(theta_0, theta_1, data):
    """ Calcula o erro quadratico medio
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
        [ 5.5277   9.1302 ]
        [ 8.5186  13.662  ]
        [ 7.0032  11.854  ]

    :return: float - o erro quadratico medio
    """
    x,y = 0, 1 
    data_len = len(data)
    media = np.mean(data)
    std = np.std(data)
    #data = (data - media) / std
    mse = np.sum([(data[i][y] - theta_0 + data[i][x] * theta_1)**2 for i in range(data_len)]) / data_len
    return mse


def step_gradient(theta_0, theta_1, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de theta_0 e theta_1.
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de theta_0 e theta_1, respectivamente
    """
    h = lambda x: theta_1 * x + theta_0
    data_len = len(data)
    x,y = 0, 1

    # derivadas
    t0d = 2/data_len * np.sum([h(data[i][x]) - data[i][y] for i in range(data_len)])
    t1d = 2/data_len * np.sum([(h(data[i][x]) - data[i][y]) * data[i][x] for i in range(data_len)])

    # step
    new_theta_0 = theta_0 - t0d * alpha
    new_theta_1 = theta_1 - t1d * alpha

    return new_theta_0, new_theta_1


def fit(data, theta_0, theta_1, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de theta_0 e theta_1.
    Ao final, retorna duas listas, uma com os theta_0 e outra com os theta_1
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param theta_0: float - intercepto da reta
    :param theta_1: float -inclinacao da reta
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os theta_0 e outra com os theta_1 obtidos ao longo da execução
    """

    theta_0_list, theta_1_list = [], []

    for _ in range(num_iterations):
      theta_0, theta_1 = step_gradient(theta_0,theta_1,data,alpha)
      theta_0_list.append(theta_0)
      theta_1_list.append(theta_1)

    return theta_0_list, theta_1_list
