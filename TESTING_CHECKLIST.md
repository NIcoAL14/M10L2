# 🧪 Lista de Control de Pruebas - ClimateNews AI

## 📋 Objetivos de Pruebas

Este documento define las pruebas necesarias para verificar que **ClimateNews AI** funciona correctamente según las especificaciones del proyecto. Los objetivos principales son:

- ✅ Verificar que la aplicación carga y funciona sin errores
- ✅ Validar que todas las funcionalidades principales operan correctamente
- ✅ Asegurar que la interfaz de usuario es intuitiva y funcional
- ✅ Comprobar que las APIs responden correctamente
- ✅ Validar que la base de datos gestiona los datos adecuadamente
- ✅ Verificar que las visualizaciones de datos se renderizan correctamente

---

## 🎯 Categorías de Pruebas

### 1. FUNCIONALIDAD (Prioridad: ALTA)

#### 1.1 Inicialización y Configuración
- [ ] **La aplicación Flask inicia correctamente sin errores**
  - **Resultado esperado:** Al ejecutar `python app.py`, el servidor arranca sin errores y muestra mensaje de inicio
  - **Pasos:**
    1. Abrir terminal en el directorio del proyecto
    2. Ejecutar `python app.py`
    3. Verificar que no hay errores en la consola
    4. Confirmar que el servidor está corriendo en el puerto especificado

- [ ] **La base de datos se inicializa correctamente**
  - **Resultado esperado:** La tabla `news` se crea automáticamente si no existe
  - **Pasos:**
    1. Eliminar el archivo `climate_news.db` si existe
    2. Ejecutar la aplicación
    3. Verificar que se crea el archivo de base de datos
    4. Usar SQLite para confirmar que la tabla `news` existe con las columnas correctas

#### 1.2 Rutas y Navegación
- [ ] **La página principal (index) carga correctamente**
  - **Resultado esperado:** Al acceder a `/`, se muestra la página de inicio con el título "ClimateNews AI" y las secciones de características
  - **Pasos:**
    1. Iniciar la aplicación
    2. Abrir navegador en `http://localhost:5000/`
    3. Verificar que la página carga completamente
    4. Confirmar que el título, navegación y sección hero son visibles

- [ ] **El dashboard carga correctamente**
  - **Resultado esperado:** Al acceder a `/dashboard`, se muestra el dashboard con las tarjetas de estadísticas y gráficos
  - **Pasos:**
    1. Navegar a `http://localhost:5000/dashboard`
    2. Verificar que el dashboard carga sin errores
    3. Confirmar que las tarjetas de estadísticas se muestran
    4. Verificar que el contenedor de gráficos está presente

- [ ] **Los enlaces de navegación funcionan**
  - **Resultado esperado:** Los enlaces "Inicio" y "Dashboard" navegan correctamente entre páginas
  - **Pasos:**
    1. En la página principal, hacer clic en "Dashboard"
    2. Verificar que se redirige al dashboard
    3. En el dashboard, hacer clic en "Inicio"
    4. Verificar que se redirige a la página principal

#### 1.3 APIs
- [ ] **La API `/api/news` responde correctamente**
  - **Resultado esperado:** La API devuelve un JSON con las últimas 20 noticias ordenadas por fecha
  - **Pasos:**
    1. Navegar a `http://localhost:5000/api/news` o usar curl
    2. Verificar que la respuesta es un JSON válido
    3. Confirmar que contiene un array de objetos con las propiedades: id, title, content, source, date, impact_level, keywords
    4. Verificar que las noticias están ordenadas por fecha descendente

- [ ] **La API `/api/stats` responde correctamente**
  - **Resultado esperado:** La API devuelve un JSON con el conteo de noticias por nivel de impacto
  - **Pasos:**
    1. Navegar a `http://localhost:5000/api/stats` o usar curl
    2. Verificar que la respuesta es un JSON válido
    3. Confirmar que contiene claves para los niveles de impacto (alto, medio, bajo)
    4. Verificar que los valores son números enteros

#### 1.4 Base de Datos
- [ ] **La base de datos acepta inserciones de noticias**
  - **Resultado esperado:** Se pueden insertar noticias en la base de datos sin errores
  - **Pasos:**
    1. Usar SQLite o un script de prueba para insertar una noticia de ejemplo
    2. Verificar que la inserción fue exitosa
    3. Consultar la base de datos para confirmar que la noticia existe
    4. Verificar que todos los campos fueron guardados correctamente

- [ ] **La base de datos maneja correctamente campos nulos**
  - **Resultado esperado:** La base de datos acepta noticias con campos opcionales vacíos (content, keywords)
  - **Pasos:**
    1. Insertar una noticia sin el campo `content`
    2. Insertar una noticia sin el campo `keywords`
    3. Verificar que ambas inserciones son exitosas
    4. Confirmar que las consultas devuelven correctamente estos registros

---

### 2. INTERFAZ DE USUARIO (Prioridad: ALTA)

#### 2.1 Diseño y Estilos
- [ ] **La página principal se ve correctamente en diferentes tamaños de pantalla**
  - **Resultado esperado:** El diseño es responsive y se adapta a pantallas de escritorio, tablet y móvil
  - **Pasos:**
    1. Abrir la aplicación en diferentes tamaños de ventana (1920x1080, 1366x768, 768x1024, 375x667)
    2. Verificar que el contenido se ajusta correctamente
    3. Confirmar que no hay desbordamiento horizontal
    4. Verificar que la navegación sigue siendo usable en pantallas pequeñas

- [ ] **Los colores y estilos CSS se aplican correctamente**
  - **Resultado esperado:** La página muestra el gradiente de fondo, los botones tienen el estilo correcto, y las tarjetas tienen sombras y bordes apropiados
  - **Pasos:**
    1. Inspeccionar los elementos en el navegador
    2. Verificar que las clases CSS están siendo aplicadas
    3. Confirmar que el gradiente de fondo es visible
    4. Verificar que los botones tienen el hover effect

#### 2.2 Interactividad
- [ ] **El botón "Ver Dashboard" funciona**
  - **Resultado esperado:** Al hacer clic en el botón, se navega al dashboard
  - **Pasos:**
    1. En la página principal, hacer clic en el botón "Ver Dashboard"
    2. Verificar que se redirige a `/dashboard`
    3. Confirmar que el dashboard carga completamente

- [ ] **Las tarjetas de estadísticas del dashboard se actualizan**
  - **Resultado esperado:** Las tarjetas muestran los valores correctos obtenidos de la API
  - **Pasos:**
    1. Navegar al dashboard
    2. Esperar a que los datos carguen
    3. Verificar que las tarjetas muestran números (no "0" si hay datos)
    4. Confirmar que los valores coinciden con los datos de la API

#### 2.3 Visualizaciones
- [ ] **El gráfico de impacto se renderiza correctamente**
  - **Resultado esperado:** El gráfico de pastel muestra la distribución de noticias por nivel de impacto
  - **Pasos:**
    1. Navegar al dashboard
    2. Verificar que el contenedor `impact-chart` no está vacío
    3. Confirmar que Plotly renderiza el gráfico de pastel
    4. Verificar que las etiquetas "Alto", "Medio", "Bajo" son visibles

- [ ] **La lista de noticias se muestra correctamente**
  - **Resultado esperado:** Las noticias se muestran en tarjetas con título, fuente, fecha y badge de impacto
  - **Pasos:**
    1. Navegar al dashboard
    2. Verificar que el contenedor de noticias no está vacío (si hay datos)
    3. Confirmar que cada noticia tiene título, fuente, fecha y badge
    4. Verificar que los badges de impacto tienen los colores correctos (rojo para alto, naranja para medio, verde para bajo)

---

### 3. FUNCIONALIDADES ESPECÍFICAS (Prioridad: MEDIA)

#### 3.1 Web Scraping / API de Noticias
- [ ] **El sistema puede obtener noticias de fuentes externas**
  - **Resultado esperado:** La aplicación puede conectarse a una API de noticias o hacer scraping de sitios web
  - **Pasos:**
    1. Ejecutar el módulo de scraping (cuando esté implementado)
    2. Verificar que no hay errores de conexión
    3. Confirmar que se obtienen noticias reales
    4. Verificar que los datos tienen el formato esperado

- [ ] **El sistema maneja errores de conexión correctamente**
  - **Resultado esperado:** Si falla la conexión a una API externa, la aplicación no crashea y muestra un mensaje apropiado
  - **Pasos:**
    1. Simular un error de conexión (desconectar internet o usar URL inválida)
    2. Verificar que la aplicación maneja el error gracefully
    3. Confirmar que se muestra un mensaje de error apropiado
    4. Verificar que la aplicación sigue funcionando para otras funcionalidades

#### 3.2 Procesamiento NLP
- [ ] **El sistema clasifica el impacto ambiental correctamente**
  - **Resultado esperado:** Las noticias se clasifican en alto, medio o bajo impacto según su contenido
  - **Pasos:**
    1. Proveer noticias de ejemplo con diferentes niveles de impacto
    2. Ejecutar el módulo de clasificación
    3. Verificar que las clasificaciones son lógicas
    4. Confirmar que el campo `impact_level` se actualiza correctamente

- [ ] **El sistema extrae keywords relevantes**
  - **Resultado esperado:** El sistema identifica palabras clave relacionadas con el cambio climático
  - **Pasos:**
    1. Proveer un texto sobre cambio climático
    2. Ejecutar el módulo de extracción de keywords
    3. Verificar que las keywords están relacionadas con el clima
    4. Confirmar que las keywords se guardan en la base de datos

#### 3.3 Nubes de Palabras
- [ ] **La nube de palabras se genera correctamente**
  - **Resultado esperado:** Se genera una imagen de nube de palabras con las keywords más frecuentes
  - **Pasos:**
    1. Ejecutar el módulo de generación de nube de palabras
    2. Verificar que se genera una imagen
    3. Confirmar que las palabras son legibles
    4. Verificar que el tamaño de las palabras refleja su frecuencia

---

### 4. RENDIMIENTO (Prioridad: MEDIA)

#### 4.1 Tiempo de Carga
- [ ] **La página principal carga en menos de 2 segundos**
  - **Resultado esperado:** El tiempo de carga de la página principal es aceptable
  - **Pasos:**
    1. Usar herramientas de desarrollo del navegador para medir el tiempo de carga
    2. Cargar la página principal varias veces
    3. Verificar que el tiempo promedio es menor a 2 segundos
    4. Anotar el tiempo promedio

- [ ] **El dashboard carga en menos de 3 segundos**
  - **Resultado esperado:** El tiempo de carga del dashboard (incluyendo API calls) es aceptable
  - **Pasos:**
    1. Usar herramientas de desarrollo para medir el tiempo de carga
    2. Cargar el dashboard varias veces
    3. Verificar que el tiempo promedio es menor a 3 segundos
    4. Anotar el tiempo promedio

#### 4.2 Uso de Recursos
- [ ] **La aplicación no consume memoria excesiva**
  - **Resultado esperado:** El uso de memoria de la aplicación es razonable
  - **Pasos:**
    1. Usar un monitor de recursos del sistema
    2. Observar el uso de memoria mientras la aplicación corre
    3. Verificar que no hay fugas de memoria
    4. Confirmar que el uso se mantiene estable

---

### 5. SEGURIDAD (Prioridad: BAJA)

#### 5.1 Validación de Datos
- [ ] **La API valida datos de entrada**
  - **Resultado esperado:** La API rechaza datos malformados o inseguros
  - **Pasos:**
    1. Enviar datos inválidos a las APIs (cuando estén implementadas)
    2. Verificar que se devuelve un error apropiado
    3. Confirmar que los datos inválidos no se guardan en la base de datos

#### 5.2 Protección de Datos
- [ ] **No se exponen credenciales en el código**
  - **Resultado esperado:** Las API keys y credenciales están en variables de entorno o archivos de configuración
  - **Pasos:**
    1. Revisar el código fuente
    2. Verificar que no hay API keys hardcodeadas
    3. Confirmar que se usa `.env` o variables de entorno para credenciales

---

### 6. EXPERIENCIA DE USUARIO (Prioridad: MEDIA)

#### 6.1 Mensajes de Error
- [ ] **Los mensajes de error son claros y útiles**
  - **Resultado esperado:** Cuando ocurre un error, el usuario recibe un mensaje explicativo
  - **Pasos:**
    1. Simular diferentes errores (API down, base de datos inaccesible, etc.)
    2. Verificar que se muestran mensajes de error apropiados
    3. Confirmar que los mensajes son comprensibles para el usuario

#### 6.2 Navegación Intuitiva
- [ ] **La navegación es intuitiva**
  - **Resultado esperado:** El usuario puede navegar fácilmente entre secciones
  - **Pasos:**
    1. Pedir a un usuario (no desarrollador) que use la aplicación
    2. Observar si puede encontrar las funcionalidades principales
    3. Verificar que no hay confusión sobre cómo navegar
    4. Confirmar que los enlaces son descriptivos

---

## 📊 Matriz de Prioridades

| Categoría | Prioridad | Orden Sugerido |
|-----------|-----------|----------------|
| Funcionalidad (Inicialización) | ALTA | 1 |
| Funcionalidad (Rutas) | ALTA | 2 |
| Interfaz de Usuario | ALTA | 3 |
| Funcionalidad (APIs) | ALTA | 4 |
| Funcionalidad (Base de Datos) | ALTA | 5 |
| Funcionalidades Específicas | MEDIA | 6 |
| Rendimiento | MEDIA | 7 |
| Experiencia de Usuario | MEDIA | 8 |
| Seguridad | BAJA | 9 |

---

## ✅ Criterios de Aprobación

Para considerar que el proyecto ha pasado las pruebas exitosamente:

- ✅ Todas las pruebas de prioridad ALTA deben pasar
- ✅ Al menos el 80% de las pruebas de prioridad MEDIA deben pasar
- ✅ Las pruebas de prioridad BAJA son opcionales pero recomendadas
- ✅ No debe haber errores críticos que impidan el uso de la aplicación
- ✅ La interfaz debe ser funcional en al menos un navegador moderno

---

## 📝 Registro de Pruebas

| Fecha | Prueba | Resultado | Observaciones | Responsable |
|-------|--------|-----------|----------------|--------------|
| | | | | |
| | | | | |
| | | | | |
| | | | | |

---

## 🐛 Reporte de Errores

Si se encuentra algún error durante las pruebas, documentarlo aquí:

| ID | Descripción | Severidad | Estado | Solución Propuesta |
|----|-------------|-----------|--------|-------------------|
| | | | | |
| | | | | |
| | | | | |

---

## 🔄 Iteraciones de Pruebas

- **Iteración 1:** Pruebas funcionales básicas (inicialización, rutas, navegación)
- **Iteración 2:** Pruebas de APIs y base de datos
- **Iteración 3:** Pruebas de funcionalidades específicas (scraping, NLP, nubes de palabras)
- **Iteración 4:** Pruebas de interfaz de usuario y experiencia de usuario
- **Iteración 5:** Pruebas de rendimiento y seguridad

---

**Última actualización:** 23 de Octubre de 2026
**Versión:** 1.0
