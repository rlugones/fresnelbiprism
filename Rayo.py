import numpy as np
import matplotlib.pyplot as plt

class Rayo(object):
  def __init__(self, angProp):
    self.angPropIni = angProp
    self.angProp = angProp

  def inicializar(self):
    self.cambiarAngProp(self.angPropIni)

  def getAngProp(self):
    return self.angProp

  def cambiarAngProp(self, new_angProp):
    self.angProp = new_angProp
