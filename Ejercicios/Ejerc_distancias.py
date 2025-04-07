import numpy as np
import pandas as pd
from scipy.spatial import distance

# Definir las coordenadas de las tiendas correctamente
puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1),
}

# Convertir las coordenadas a un DataFrame
df_puntos = pd.DataFrame.from_dict(puntos, orient='index', columns=['X', 'Y'])
print('Coordenadas de los puntos:')
print(df_puntos)

def calcular_distancias(df, funcion_distancia):
    distancias = pd.DataFrame(index=df.index, columns=df.index)

    for i in df.index:
        for j in df.index:
            if i != j:
                distancias.loc[i, j] = funcion_distancia(df.loc[i], df.loc[j])
            else:
                distancias.loc[i, j] = 0  # La distancia a sí mismo es 0
    return distancias 

# Calcular distancias
dist_euclidiana = calcular_distancias(df_puntos, distance.euclidean)
dist_manhattan = calcular_distancias(df_puntos, distance.cityblock)
dist_chebyshev = calcular_distancias(df_puntos, distance.chebyshev)

# Encontrar la distancia máxima en cada métrica
valor_maximo_euclidiana = dist_euclidiana.max().max()
puntoA_euclidiana, puntoB_euclidiana = dist_euclidiana.stack().idxmax()

valor_maximo_manhattan = dist_manhattan.max().max()
puntoA_manhattan, puntoB_manhattan = dist_manhattan.stack().idxmax()

valor_maximo_chebyshev = dist_chebyshev.max().max()
puntoA_chebyshev, puntoB_chebyshev = dist_chebyshev.stack().idxmax()

# Imprimir resultados
print('\n--- Tabla de distancias Euclidianas ---')
print(dist_euclidiana)
print(f'\nDistancia máxima euclidiana: {valor_maximo_euclidiana}')
print(f'Entre punto {puntoA_euclidiana} y el punto {puntoB_euclidiana}')

print('\n--- Tabla de distancias Manhattan ---')
print(dist_manhattan)
print(f'\nDistancia máxima Manhattan: {valor_maximo_manhattan}')
print(f'Entre punto {puntoA_manhattan} y el punto {puntoB_manhattan}')

print('\n--- Tabla de distancias Chebyshev ---')
print(dist_chebyshev)
print(f'\nDistancia máxima Chebyshev: {valor_maximo_chebyshev}')
print(f'Entre punto {puntoA_chebyshev} y el punto {puntoB_chebyshev}')
