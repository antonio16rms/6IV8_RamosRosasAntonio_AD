import numpy as np
import matplotlib.pyplot as plt

#Vamos a crear una semilla random para reproducibilidad
np.random.seed(16)

#Vamos a buscar los parametros para una distribucion
#Media
media = 0
#Desviaciones estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#El numero de muestras para el analisis
n_muestras = 1000

#Vamos a generar los datos de las distribuciones normales
data1 = np.random.normal(media, sigma1, n_muestras)
data2 = np.random.normal(media, sigma2, n_muestras)
data3 = np.random.normal(media, sigma3, n_muestras)

#Vamos a configurar la grafica
plt.figure(figsize=(10,6))

#Vamos a cargar las frecuencias a partir de una graifca de histograma
plt.hist(data1, bins=30, color='r', density=True, label='Desviacion estandar 1', alpha=0.5)
plt.hist(data2, bins=30, color='g', density=True, label='Desviacion estandar 2', alpha=0.5)
plt.hist(data3, bins=30, color='b', density=True, label='Desviacion estandar 3', alpha=0.5)

#A grafiar
plt.title('Comparacion de Distribuciones Normales con una semilla en random')
plt.xlabel('Valor')
plt.ylabel('Densidad')
plt.axhline(0, color='black', linewidth=0.5, ls='--')
plt.axvline(0, color='black', linewidth=0.5, ls='--')
plt.legend()
plt.grid()

plt.show()