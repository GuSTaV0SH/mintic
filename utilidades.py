""" Modulo generador aleatorio de cadenas #
    Funciones que retornan criaturas marinas
    y ubicaciones del barco 
    F. Gustavo Sierra Hernández
    Mayo 23 2021 """

import random
def aparecer_criatura():
  """ 
  Returns
  -------
  criatura:str
  Una de las 8 criaturas de la lista generadas aleatoriamente     
  """
  criaturas=["un Kraken","unas Sirenas","una Ballena","un Hipocampo","una Macaraprono","un Pulpo","unos Leviatanes","Unas Hidras"]
  indice = random.randint(0, 7)
  return criaturas[indice]

def aparecer_direccion():
  """ 
  Returns
  -------
  criatura:str
  Una de las 4 direcciones de la lista generadas aleatoriamente     
  """
  direccion=["A babor","A estribor","Por la proa","Por la popa"]
  indice = random.randint(0, 3)
  return direccion[indice]


