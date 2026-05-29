
# =============================================================================
# Análisis de Datos Climáticos Globales
# UTN - Organización Empresarial 2026
# Autor: Pablo Kunz (P2 - Desarrollador Técnico)
# Revisión y documentación: Pablo Kunz (P3 - Revisor QA)
# =============================================================================

import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset desde la carpeta /datos
# Se utiliza ruta relativa para garantizar reproducibilidad en cualquier entorno
df = pd.read_csv('datos/dataset.csv')

# Verificamos la carga correcta mostrando las primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Filtramos por la fuente GCAG para evitar duplicados en el análisis
# GCAG: Global Change Attribution Group - fuente principal del dataset
df_gcag = df[df['Source'] == 'GCAG'].copy()

# Calculamos indicadores estadísticos básicos sobre la columna Mean
# Los valores representan anomalías de temperatura respecto a la media histórica
print("\nIndicadores de temperatura (anomalías respecto a media histórica):")
print(f"Temperatura promedio: {df_gcag['Mean'].mean():.4f}")
print(f"Temperatura máxima: {df_gcag['Mean'].max():.4f}")
print(f"Temperatura mínima: {df_gcag['Mean'].min():.4f}")

# Generamos gráfico de evolución temporal de la anomalía de temperatura
# Se guarda en /resultados para mantener la estructura del repositorio
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
