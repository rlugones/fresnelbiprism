class Rayo(object):
  """
  Clase Rayo. Un objeto de Rayo tiene un angulo de propagacion y puede
  cambiar dicho angulo.
  """
  def __init__(self, angProp):
    self.angPropIni = angProp
    self.angProp = angProp

  def reinicializar(self):
    """
    Reinicializa el angulo de propagacion.
    """
    self.cambiarAngProp(self.angPropIni)

  def getAngProp(self):
    return self.angProp

  def cambiarAngProp(self, new_angProp):
    """
    Cambia el angulo en con el que el rayo se esta propagando.
    """
    self.angProp = new_angProp
