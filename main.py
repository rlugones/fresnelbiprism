import numpy as np
import matplotlib.pyplot as plt
from Medio import Medio
from Rayo import Rayo
from DioptraPlana import DioptraPlana
plt.ion()

alpha1 = 10/180*np.pi
medio = Medio(5)
medio.agregarElemento(DioptraPlana(1, 4/3), 1)
medio.agregarElemento(DioptraPlana(4/3, 1, alpha1), 1.01)
dx = 0.01

for beta in range(10):
  beta = beta/180*np.pi
  rayo = Rayo(beta)
  medio.dibujar(dx, rayo)

plt.savefig('propagacion.png')
