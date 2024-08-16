# -*- coding: utf-8 -*-
"""Involuta de la catenaria (tractiz).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Oo1mS1RFbRC4_HSeKUNis9MlkkGxXLR-
"""

import numpy as np
import matplotlib.pyplot as plt


a = 1


x = np.linspace(-2, 4, 1000)
y_catenary = a * np.cosh(x / a)


y_tractrix = a * np.log((a + np.sqrt(a**2 - x**2)) / x) - np.sqrt(a**2 - x**2)


plt.figure(figsize=(10, 6))


plt.plot(x, y_catenary, label='Catenaria', color='blue')
plt.plot(x, y_tractrix, label='Tractriz', color='orange')

# etiquetas y título
plt.xlabel('x')
plt.ylabel('y')
plt.title('Catenaria y su involuta (tractriz)')


plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()



#Analizando la grafica puedo decir que La catenaria se grafica como una curva simétrica respecto al eje y, mientras que su involuta (tractriz) se aproxima al eje x asintóticamente.

