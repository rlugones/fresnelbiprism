import numpy as np
import matplotlib.pyplot as plt

class DioptraPlana(object):
  def __init__(self, nInc, nProp, inclinacion=0):
    self.nInc = nInc
    self.nProp = nProp
    self.inclinacion = inclinacion

  def cambiarProp(self, angInc):
    return -np.arcsin(self.nInc/self.nProp * np.sin(self.inclinacion-angInc)) + self.inclinacion
