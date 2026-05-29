
# Análisis de Datos Climáticos Globales
# UTN - Organización Empresarial 2026
# Autor: Pablo Kunz (P2 - Desarrollador Técnico)

import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset desde la carpeta /datos
df = pd.read_csv('datos/dataset.csv')

# Mostramos las primeras filas para verificar la carga
print("Primeras filas del dataset:")
print(df.head())

# Filtramos solo una fuente para evitar duplicados
df_gcag = df[df['Source'] == 'GCAG'].copy()

# Calculamos indicadores básicos de temperatura (columna Mean)
print("\nIndicadores de temperatura (anomalías respecto a media histórica):")
print(f"Temperatura promedio: {df_gcag['Mean'].mean():.4f}")
print(f"Temperatura máxima: {df_gcag['Mean'].max():.4f}")
print(f"Temperatura mínima: {df_gcag['Mean'].min():.4f}")

# Generamos gráfico de evolución de temperatura
plt.figure(figsize=(12, 5))
plt.plot(df_gcag['Year'], df_gcag['Mean'], color='tomato', linewidth=0.8)
plt.title('Evolución de la Anomalía de Temperatura Global (GCAG)')
plt.xlabel('Fecha')
plt.ylabel('Anomalía de Temperatura (°C)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('resultados/grafico_temperatura.png')
plt.show()
print("Gráfico guardado en /resultados")
