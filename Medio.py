import numpy as np
import matplotlib.pyplot as plt

class Medio(object):
  """
  Clase Medio. Un objeto de Medio es donde se va a propagar un
  objeto de Rayo.
  """
  def __init__(self, tamano=10):
    self.tamano = tamano
    self.elementos = []

  def agregarElemento(self, elemento, posicion):
    """
    Agrega elementos opticos al medio en una posicion dada.
    """
    self.elementos.append([elemento, posicion])

  def propagar(self, dx, rayo):
    """
    Propaga el rayo en el medio, pasando por todos sus elementos opticos.
    """
    rayo.reinicializar()
    x = np.arange(0, self.tamano, dx)
    y = np.zeros(len(x))
    for i, xi in enumerate(x):
      if i == 0: continue
      for [elem, xj] in self.elementos:
        if xi == xj:
          rayo.cambiarAngProp(elem.cambiarProp(rayo.getAngProp()))
      y[i] = y[i-1] + dx * np.tan(rayo.getAngProp())
    return [x, y]

  def extenderRayos(self, dx, rayo):
    """
    Calcula la extension del rayo, a partir del angulo final de propagacion.
    """
    xExt = np.arange(0-self.tamano/10, self.tamano, dx)
    [x, y] = self.propagar(dx, rayo)
    dy = y[-1]-y[-2]
    yExt = np.zeros(len(xExt))
    yExt[-1] = y[-1]
    for i in range(len(yExt)-1, 0, -1):
      yExt[i-1] = yExt[i] - dy
    return [xExt, yExt]


  def dibujar(self, dx, rayo):
    """
    Grafica la propagacion del rayo y su extension
    """
    [x, y] = self.propagar(dx, rayo)
    [xExt, yExt] = self.extenderRayos(dx, rayo)
    plt.plot(x, y)
    plt.plot(xExt, yExt, ':')
    plt.title('Propagación de rayos en parte superior')
