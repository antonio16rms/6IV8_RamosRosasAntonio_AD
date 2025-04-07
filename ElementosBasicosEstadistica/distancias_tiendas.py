import numpy as np
import pandas as pd
from scipy.spatial import distance

# Definir las coordenadas de las tiendas correctamente
tiendas = {
    'Tienda A': (1, 1),
    'Tienda B': (1, 5),
    'Tienda C': (7, 1),
    'Tienda D': (3, 3),
    'Tienda E': (4, 8),
}

# Convertir las coordenadas a un DataFrame
df_tiendas = pd.DataFrame.from_dict(tiendas, orient='index', columns=['X', 'Y'])
print('Coordenadas de las tiendas:')
print(df_tiendas, "\n")

# Inicializar dataframes para almacenar las distancias
distancias_eu = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_mh = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)
distancias_ch = pd.DataFrame(index=df_tiendas.index, columns=df_tiendas.index)

# Calcular las distancias entre las tiendas
for i in df_tiendas.index:
    for j in df_tiendas.index:
        coord_i = df_tiendas.loc[i].values
        coord_j = df_tiendas.loc[j].values 

# Calcular las distancias
        distancias_eu.loc[i, j] = distance.euclidean(coord_i, coord_j)
        distancias_mh.loc[i, j] = distance.cityblock(coord_i, coord_j)
        distancias_ch.loc[i, j] = distance.chebyshev(coord_i, coord_j)

# Mostrar los resultados
print('Distancias Euclidianas:')
print(distancias_eu, "\n")
print('Distancias Manhattan:')
print(distancias_mh, "\n")
print('Distancias Chebyshev:')
print(distancias_ch, "\n")
