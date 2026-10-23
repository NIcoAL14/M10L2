# 🌍 Proyecto Hackathon - Cambio Climático

## 📝 Nombre del Proyecto

**ClimateNews AI**

## 🔍 ¿En qué consiste?

Es una plataforma web que utiliza inteligencia artificial para analizar noticias sobre el cambio climático en tiempo real de múltiples fuentes. El sistema identifica tendencias, genera nubes de palabras, clasifica noticias por impacto ambiental y proporciona un dashboard interactivo con visualizaciones de datos. Además, incluye **alertas climáticas en tiempo real de todo el mundo** mediante integración con WeatherAPI, un **mapa interactivo del mundo** donde puedes hacer clic en cualquier ubicación para ver el clima detallado, un generador de resúmenes automáticos y alertas sobre eventos climáticos importantes para mantener a los usuarios informados y concienciados.

## 🎯 ¿Qué problema resuelve?

La desinformación y la sobrecarga de información sobre el cambio climático. Existen miles de noticias sobre el clima diariamente, pero es difícil para las personas saber qué es relevante, distinguir entre información fiable y sensacionalismo, y comprender las tendencias globales. ClimateNews AI resuelve esto filtrando, analizando y presentando la información de manera clara, basada en datos y accesible, permitiendo a los usuarios tomar decisiones informadas y mantenerse actualizados sobre lo que realmente importa en la lucha contra el cambio climático.

## 🎨 Este es el tipo de mi proyecto:
> Plataforma web con Flask + NLP + Visualización de datos + Base de datos

## 📚 Las bibliotecas que voy a utilizar:
- **Flask** - Framework web para crear la aplicación
- **BeautifulSoup4** - Web scraping para extraer noticias de sitios web
- **Requests** - Consumir APIs de noticias (NewsAPI, etc.) y WeatherAPI
- **NLTK** - Procesamiento de lenguaje natural para clasificación de texto
- **SpaCy** - Análisis de texto avanzado y extracción de entidades
- **WordCloud** - Generación de nubes de palabras
- **Plotly** - Visualización de datos interactiva
- **Matplotlib** - Gráficos estáticos
- **Pandas** - Manejo de datos en tablas
- **NumPy** - Cálculos numéricos
- **python-dotenv** - Gestión de variables de entorno para API keys

## 🔗 Referencias útiles:
- [Newswire - News Dashboard con Flask](https://github.com/szymon42069/Newswire) - Dashboard de noticias que scrappea RSS feeds de Google News y los sirve a través de una API Flask
- [PyCast News - News Aggregator](https://asbinthapa99.github.io/news/) - Agregador de noticias automatizado con Flask y PostgreSQL que scrappea 14 feeds RSS cada hora
- [Flask News Application con NewsAPI](https://www.geeksforgeeks.org/python/flask-news-application-using-newsapi/) - Tutorial completo para crear una app de noticias con Flask y NewsAPI
- [WeatherAPI Documentation](https://www.weatherapi.com/docs/) - Documentación oficial de WeatherAPI para obtener datos climáticos y alertas

## � Los artículos de la guía que me ayudarán durante el desarrollo:
- [NLTK Learning to Classify Text](https://www.nltk.org/book/ch06.html) - Explica cómo usar NLTK para clasificar texto con técnicas de machine learning como Naive Bayes y Decision Trees, perfecto para clasificar noticias por impacto ambiental
- [NLTK Classification How-To](https://www.nltk.org/howto/classify.html) - Documentación práctica sobre cómo implementar clasificadores de texto con NLTK
- [Integrate Plotly Dash Into Flask](https://hackersandslackers.com/plotly-dash-with-flask/) - Guía para integrar visualizaciones interactivas de Plotly dentro de aplicaciones Flask
- [Plotly NanoDash Tutorial](https://github.com/plotly/tutorial-nanodash) - Tutorial que enseña cómo construir dashboards interactivos desde cero con Flask y Plotly.js

## 🚀 Funcionalidades

- **Análisis de noticias en tiempo real** de múltiples fuentes
- **Clasificación por impacto ambiental** (alto, medio, bajo)
- **Nubes de palabras** para identificar temas recurrentes
- **Dashboard interactivo** con visualizaciones de datos
- **Mapa climático interactivo del mundo** - Haz clic en cualquier ubicación para ver clima detallado
- **Datos climáticos en tiempo real** - Temperatura, humedad, viento, presión, UV, calidad del aire
- **Pronóstico de 7 días** para cualquier ubicación del mundo
- **Generador de resúmenes automáticos** con IA
- **Alertas climáticas en tiempo real** de ciudades principales del mundo (via WeatherAPI)
- **Detección de condiciones extremas** (olas de calor, frío, vientos fuertes, lluvia intensa)
- **Búsqueda inteligente** por temas y keywords

## 📦 Instalación

```bash
# 1. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Configurar API keys
cp .env.example .env
# Editar .env y agregar tu API key de WeatherAPI
# Obtén tu API key gratuita en: https://www.weatherapi.com/

# 4. Ejecutar la aplicación
python app.py
```

### Configuración de WeatherAPI

Para utilizar las alertas climáticas en tiempo real, necesitas una API key de WeatherAPI:

1. Regístrate gratis en [WeatherAPI](https://www.weatherapi.com/)
2. Copia tu API key
3. Crea un archivo `.env` en el directorio del proyecto
4. Agrega tu API key: `WEATHER_API_KEY=tu_api_key_aqui`

Sin la API key, la aplicación funcionará pero no mostrará alertas climáticas en tiempo real.

## 📊 Contribución

Este proyecto es parte de un hackathon enfocado en soluciones para el cambio climático.

## 📄 Licencia

MIT License
