import numpy as np

class DioptraPlana(object):
  """
  Clase DioptraPlana. Un objeto de DioptraPlana representa una
  dioptra plana, con eventualmente una inclinacion.
  """
  def __init__(self, nInc, nProp, inclinacion=0):
    self.nInc = nInc
    self.nProp = nProp
    self.inclinacion = inclinacion

  def cambiarProp(self, angInc):
    """
    Calcula el nuevo angulo con en el que se propaga el rayo.
    """
    return -np.arcsin(self.nInc/self.nProp * np.sin(self.inclinacion-angInc)) + self.inclinacion
