Análisis Exploratorio de Anuncios de Vehículos en EE. UU.
📌 Resumen ejecutivo
Este proyecto consistió en el desarrollo de una aplicación web interactiva utilizando Streamlit, con el objetivo de analizar un conjunto de datos públicos de anuncios de coches usados en Estados Unidos. A través de un análisis exploratorio de datos (EDA), se identificaron patrones relevantes en variables como el precio, el año del modelo y el tipo de combustible.

La herramienta permite a cualquier usuario explorar visualmente estos datos mediante histogramas y gráficos de dispersión construidos con plotly-express.

🎯 Objetivo del estudio
Brindar una comprensión visual clara y accesible sobre las características principales del mercado de autos usados en EE. UU., detectando:

La distribución de precios predominantes.

El tipo de combustible más común.

La relación entre el precio y el año del modelo.

📊 Resultados principales
Distribución de precios
La mayoría de los vehículos listados se ofrecen por debajo de los $20,000 USD, con un fuerte pico en autos de bajo costo. Existen valores atípicos de hasta $350,000, aunque son casos excepcionales.

Tipo de combustible predominante
El tipo de combustible gasolina es, por amplio margen, el más utilizado en los anuncios, por encima de híbridos o diésel. Esto refleja la prevalencia de tecnologías tradicionales en el parque vehicular actual.

Relación entre precio y año del modelo
Se observa una correlación positiva entre el año del modelo y el precio del coche. A partir del año 2015, el mercado muestra una mayor dispersión de precios, indicando diversidad en marcas, tecnologías y condiciones de los vehículos.

🛠️ Herramientas utilizadas
Python 3

pandas

plotly-express

streamlit

Jupyter Notebook

GitHub y Render (para despliegue en línea)

🌐 Aplicación web
La versión desplegada de esta herramienta se encuentra disponible en:

👉 https://<tu_app>.onrender.com

📂 Estructura del repositorio
Copiar
Editar
.
├── README.md
├── app.py
├── vehicles_us.csv
├── requirements.txt
└── notebooks
    └── EDA.ipynb
✅ Conclusión
Esta herramienta demuestra cómo los datos abiertos pueden ser analizados y visualizados mediante tecnologías accesibles como Streamlit, generando valor para la toma de decisiones comerciales, de marketing o estratégicas en el sector automotriz.