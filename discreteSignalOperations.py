"""
Declaração de funçoes usadas em todos os exercicios.
"""
from numpy import arange, int16, zeros, nonzero
from typing import Tuple, List


def impseq(n0: int, n1: int, n2: int) -> Tuple[List, List]:
    """ 
    Gera x(n) = delta(n-n0); n1 <= n <= n2

    Args:
      n0(list): valor de deslocamento no tempo do impulso
      n1(int): menor valor para criar a lista com o range dos 
              valores possiveis.
      n2(int): maior valor para criar a lista com o range dos
              valores possiveis.
    
    Uso:
      (x, n) = impseq(n0, n1, n2)
    
    Returns:
      Tuple[List, List]: Tupla contendo duas listas. A primeira os valores
                        do eixo y, a segunda os valores do eixo x
    """
  
    # returna os valores espaçados no dado intervalo
    eixo_x = arange(n1, n2 + 1)

    arrayLen = len(eixo_x)

    # cria um array de 0 para ser o eixo y
    eixo_y = np.zeros(arrayLen)

    # coloca valor 1 no valor a ser deslocado
    eixo_y[n0 - n1] = 1
    
    return eixo_x, eixo_y
  
def stepseq(n0: int, n1: int, n2: int) -> Tuple[List, List]:
    """ 
    Gena x(n) = u(n-n0); n1 <= n <= n2

    Args:
      n0(list): valor de deslocamento no do degrau
      n1(int): menor valor para criar a lista com o range dos 
              valores possiveis.
      n2(int): maior valor para criar a lista com o range dos
              valores possiveis.
    
    Uso:
      (x, n) = stepseq(n0, n1, n2)
    """
    # returna os valores espaçados no dado intervalo
    eixo_x = arange(n1, n2 + 1)

    arrayLen = len(eixo_x)

    # cria um array de 0 para ser o eixo y
    eixo_y = np.zeros(arrayLen)

    # coloca valor 1 no valor a ser deslocado
    eixo_y[(n0 - n1):] = 1
    
    return eixo_x, eixo_y
  
def sigadd(y1: list, n1: list, y2: list, n2: list) -> Tuple[List, List]: 
    """
    Gera x(n) = x1(n) + x2(n)

    Args:
      y1(list): array com o sinal y1
      n1(int): eixo x do sinal y1
      y2(list): eixo y do sinal y2
      n2(int): eixo x do sinal y2
    
    Returns:
      Tuple[List, List]: Tupla contendo duas listas. A primeira os valores
                        do eixo y, a segunda os valores do eixo x
    """

    # limite de x minimo para o plot
    # é calculado comparando a posiçao 0 dos vetores n1 e n2
    minXLim = int(min(n1)) if (min(n1) < min(n2)) else int(min(n2))


    # o limite de x maximo para o plot
    # é calculado comparando as mairoes posiçoes dos vetores n1 e n2
    maxXLim = int(max(n1)) if (max(n1) > max(n2)) else int(max(n2))
   
    print(minXLim, maxXLim)
    # o tamanho do array do eixo x resultante sera o limite maximo em x
    # menos o limite minimo em x
    eixo_x = np.linspace(minXLim, maxXLim, num=(maxXLim - minXLim)+1)

    # cria um array de 0 com o tamanho do vetor final
    eixo_y1 = zeros(len(eixo_x), dtype=int)
    eixo_y2 = eixo_y1.copy()
   

    eixo_y1[nonzero((eixo_x >= min(n1)) & (eixo_x <= max(n1)))] = y1
    eixo_y2[nonzero((eixo_x >= min(n2)) & (eixo_x <= max(n2)))] = y2

    eixo_resultante = eixo_y1 + eixo_y2

    return eixo_resultante, eixo_x

def sigmult(y1: list, n1: list, y2: list, n2: list) -> Tuple[List, List]: 
    """
    Gera x(n) = x1(n) * x2(n)

    Args:
      y1(list): array com o sinal y1
      n1(int): eixo x do sinal y1
      y2(list): eixo y do sinal y2
      n2(int): eixo x do sinal y2
    
    Returns:
      Tuple[List, List]: Tupla contendo duas listas. A primeira os valores
                        do eixo y, a segunda os valores do eixo x
    """

    # limite de x minimo para o plot
    # é calculado comparando a posiçao 0 dos vetores n1 e n2
    minXLim = int(min(n1)) if (min(n1) < min(n2)) else int(min(n2))


    # o limite de x maximo para o plot
    # é calculado comparando as mairoes posiçoes dos vetores n1 e n2
    maxXLim = int(max(n1)) if (max(n1) > max(n2)) else int(max(n2))
   

    # o tamanho do array do eixo x resultante sera o limite maximo em x
    # menos o limite minimo em x
    
    eixo_x = np.linspace(minXLim, maxXLim, num=(maxXLim - minXLim)+1)

    # cria um array de 0 com o tamanho do vetor final
    eixo_y1 = zeros(len(eixo_x), dtype=int)
    eixo_y2 = eixo_y1.copy()
   

    eixo_y1[nonzero((eixo_x >= min(n1)) & (eixo_x <= max(n1)))] = y1
    eixo_y2[nonzero((eixo_x >= min(n2)) & (eixo_x <= max(n2)))] = y2

    eixo_resultante = eixo_y1 * eixo_y2

    return eixo_resultante, eixo_x

def sigshift(eixo_y: list, eixo_x: list, deslocamento: int) -> Tuple[List, List]:
    """
    Gera x(n) = x(n-no)

    Args:
      eixo_y(list): eixo y do sinal
      eixo_x(list): eixo x do sinal 
      deslocamento(int): deslocamento no eixo x
      
    Returns:
      Tuple[List, List]: Tupla contendo duas listas. A primeira os valores
                        do eixo y, a segunda os valores do eixo x
    """
    eixo_x = eixo_x + deslocamento
    return eixo_y, eixo_x

def sigfold(eixo_y: list, eixo_x: list) -> Tuple[List, List]:
    """
    Gera x(n) = x(-n)

    Args:
      eixo_y(list): eixo y do sinal
      eixo_x(list): eixo x do sinal 
      
    Returns:
      Tuple[List, List]: Tupla contendo duas listas. A primeira os valores
                        do eixo y, a segunda os valores do eixo x
    """

    # inverte o eixo x e negativa ele
    eixo_x = -eixo_x[::-1]
    # inverte o eixo y começando a contar da maior posiçao do array
    eixo_y = eixo_y[::-1]

    return eixo_y, eixo_x
