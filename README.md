# Análisis de Datos Climáticos Globales
## UTN - Organización Empresarial: Gestión Colaborativa y Control de Versiones

## 📝 Descripción del Proyecto
Aplicar un flujo de trabajo ágil y distribuido utilizando Git, GitHub y Jira como herramientas centrales de trazabilidad organizativa, operando estrictamente desde el entorno de Google Colab.

---

## 👥 Integrantes de la Célula de Desarrollo
*   Tron, Magalí (Rol: Hugo/Luis - P1/P3: Líder y Organizador/QA)
*   Kunz, Pablo (Rol: Paco - P2: Desarrollador)

---

## 🚀 Escenario Seleccionado
*   Escenario A - Análisis de Datos Climáticos

---

## 📊 Dataset Utilizado
- **Nombre:** Global Temperature Time Series (GISTEMP)
- **Descripción:** Dataset de temperatura promedio global con registros mensuales y anuales provenientes del análisis climático GISTEMP. Permite analizar tendencias de temperatura a lo largo del tiempo a nivel mundial.
- **Formato:** CSV
- **Origen:** https://datahub.io/core/global-temp
- **Licencia:** Dominio público

---

## 📁 Estructura del Repositorio
El proyecto sigue un diseño modular y reproducible estructurado de la siguiente manera:

```text
repo-proyecto/
│
├── datos/          # Almacena el dataset original en formato CSV o Excel.
├── scripts/        # Contiene los scripts funcionales con comentarios técnicos.
├── resultados/     # Gráficos y tablas exportadas de forma automática.
├── .gitignore      # Archivo de exclusión de archivos temporales y basura.
└── README.md       # Documentación general del proyecto (este archivo).

---

## ⚙️ Instrucciones de Ejecución
1. Clonar el repositorio en Google Colab:
```bash
   git clone https://github.com/{USUARIO}/{REPO}.git
```
2. Colocar el dataset descargado en la carpeta `/datos`
3. Ejecutar el script principal:
```bash
   python scripts/analisis_datos.py
```
4. Los resultados se guardarán automáticamente en `/resultados`

---

## 🔗 Trazabilidad
Este proyecto utiliza Conventional Commits vinculados a issues de Jira.  
Formato: `PROY-{N}: Descripción del cambio`
