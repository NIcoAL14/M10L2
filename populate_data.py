import sqlite3
from datetime import datetime, timedelta
import random

DB_NAME = 'climate_news.db'

def populate_sample_news():
    """Puebla la base de datos con noticias de ejemplo sobre cambio climático"""

    sample_news = [
        {
            'title': 'Ola de calor récord en Europa: temperaturas superan los 45°C',
            'content': 'El sur de Europa enfrenta una ola de calor sin precedentes con temperaturas que han superado los 45°C en varias regiones. Los expertos advierten que estos eventos extremos serán más frecuentes debido al cambio climático.',
            'source': 'Climate News Network',
            'date': '2026-10-23',
            'impact_level': 'alto',
            'keywords': 'ola de calor, temperatura, europa, cambio climático'
        },
        {
            'title': 'Nuevo informe del IPCC advierte sobre punto de no retorno',
            'content': 'El Panel Intergubernamental sobre el Cambio Climático publicó su último informe advirtiendo que el mundo se acerca peligrosamente a puntos de inflexión irreversibles. Se requiere una reducción inmediata del 45% en emisiones para 2030.',
            'source': 'IPCC Official',
            'date': '2026-10-22',
            'impact_level': 'alto',
            'keywords': 'IPCC, emisiones, punto de no retorno, informe'
        },
        {
            'title': 'Amazonía pierde 10% de su cobertura forestal en la última década',
            'content': 'Datos satelitales revelan que la Amazonía ha perdido más del 10% de su cobertura forestal en los últimos diez años. Esta pérdida representa un golpe significativo a la capacidad del planeta para absorber CO2.',
            'source': 'Amazon Watch',
            'date': '2026-10-21',
            'impact_level': 'alto',
            'keywords': 'amazonía, deforestación, co2, bosque'
        },
        {
            'title': 'Noruega anuncia inversiones en energía renovable',
            'content': 'El gobierno noruego ha anunciado un plan de inversión de 5 mil millones de euros en energía eólica y solar para 2030. El país busca acelerar su transición hacia una economía libre de combustibles fósiles.',
            'source': 'Renewable Energy World',
            'date': '2026-10-20',
            'impact_level': 'medio',
            'keywords': 'noruega, energía renovable, inversión, transición'
        },
        {
            'title': 'Glaciar de los Alpes pierde 20% de su masa en 5 años',
            'content': 'Científicos suizos reportan que los glaciares de los Alpes han perdido el 20% de su masa en los últimos cinco años debido al aumento de temperaturas. El derretimiento acelerado amenaza el suministro de agua en la región.',
            'source': 'Swiss Climate Institute',
            'date': '2026-10-19',
            'impact_level': 'alto',
            'keywords': 'glaciares, alpes, derretimiento, agua'
        },
        {
            'title': 'California implementa nuevas regulaciones de emisiones vehiculares',
            'content': 'California ha aprobado nuevas regulaciones que exigirán que todos los vehículos nuevos vendidos en el estado sean cero emisiones para 2035. La medida es parte de un esfuerzo más amplio para combatir el cambio climático.',
            'source': 'California EPA',
            'date': '2026-10-18',
            'impact_level': 'medio',
            'keywords': 'california, emisiones, vehículos, regulación'
        },
        {
            'title': 'Océanos absorben el 90% del exceso de calor del planeta',
            'content': 'Un nuevo estudio confirma que los océanos han absorbido el 90% del exceso de calor generado por las emisiones de gases de efecto invernadero. Este calentamiento oceánico tiene graves consecuencias para la vida marina.',
            'source': 'Oceanographic Institute',
            'date': '2026-10-17',
            'impact_level': 'alto',
            'keywords': 'océanos, calor, gases efecto invernadero, vida marina'
        },
        {
            'title': 'Australia lanza programa de reforestación de 1 millón de hectáreas',
            'content': 'El gobierno australiano ha iniciado un ambicioso programa de reforestación que busca plantar árboles en 1 millón de hectáreas para 2030. La iniciativa busca compensar emisiones y restaurar hábitats naturales.',
            'source': 'Australia Environment',
            'date': '2026-10-16',
            'impact_level': 'medio',
            'keywords': 'australia, reforestación, hectáreas, hábitat'
        },
        {
            'title': 'Huracán categoría 5 afecta costas del Caribe',
            'content': 'Un huracán de categoría 5 ha golpeado las costas del Caribe, causando destrucción masiva. Los meteorólogos atribuyen la intensidad de estos eventos al calentamiento de las aguas oceánicas.',
            'source': 'Caribbean Weather Service',
            'date': '2026-10-15',
            'impact_level': 'alto',
            'keywords': 'huracán, caribe, destrucción, calentamiento'
        },
        {
            'title': 'Comunidad local inicia proyecto de agricultura sostenible',
            'content': 'Una comunidad rural ha implementado técnicas de agricultura sostenible que reducen el uso de agua y pesticidas en un 60%. El proyecto sirve como modelo para otras comunidades.',
            'source': 'Local Sustainability News',
            'date': '2026-10-14',
            'impact_level': 'bajo',
            'keywords': 'agricultura, sostenibilidad, comunidad, agua'
        },
        {
            'title': 'Tech giants comprometen 100% energía renovable para 2030',
            'content': 'Las principales empresas tecnológicas han anunciado compromisos para operar con 100% energía renovable para 2030. Google, Microsoft y Apple lideran la iniciativa en el sector corporativo.',
            'source': 'Tech Climate News',
            'date': '2026-10-13',
            'impact_level': 'medio',
            'keywords': 'tecnología, energía renovable, corporativo, compromiso'
        },
        {
            'title': 'Nivel del mar sube 3.4 mm por año según mediciones',
            'content': 'Las mediciones más recientes indican que el nivel del mar está subiendo a un ritmo de 3.4 mm por año, acelerándose en comparación con décadas anteriores. Las zonas costeras enfrentan riesgos crecientes de inundación.',
            'source': 'Sea Level Research',
            'date': '2026-10-12',
            'impact_level': 'alto',
            'keywords': 'nivel del mar, inundación, zonas costeras, aceleración'
        }
    ]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for news in sample_news:
        cursor.execute('''
            INSERT INTO news (title, content, source, date, impact_level, keywords)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            news['title'],
            news['content'],
            news['source'],
            news['date'],
            news['impact_level'],
            news['keywords']
        ))

    conn.commit()
    conn.close()
    print(f"✅ Se insertaron {len(sample_news)} noticias de ejemplo")


def populate_sample_alerts():
    """Puebla la base de datos con alertas climáticas de ejemplo"""

    sample_alerts = [
        {
            'headline': 'Ola de calor extrema: 42°C',
            'severity': 'extreme',
            'description': 'Temperatura máxima de 42°C. Riesgo de golpe de calor y deshidratación.',
            'instruction': 'Manténgase hidratado, evite exposición al sol, use aire acondicionado.',
            'category': 'temperature',
            'effective': '2026-10-23',
            'expires': '2026-10-25',
            'location': 'Madrid',
            'source': 'WeatherAPI (detected)'
        },
        {
            'headline': 'Vientos fuertes: 65 km/h',
            'severity': 'high',
            'description': 'Rachas de viento de hasta 65 km/h. Riesgo de caída de árboles y daños estructurales.',
            'instruction': 'Evite salir, asegure objetos sueltos, manténgase alejado de árboles.',
            'category': 'wind',
            'effective': '2026-10-23',
            'expires': '2026-10-24',
            'location': 'London',
            'source': 'WeatherAPI (detected)'
        },
        {
            'headline': 'Lluvia intensa prevista',
            'severity': 'moderate',
            'description': 'Probabilidad de lluvia del 85%. Posibles inundaciones en zonas bajas.',
            'instruction': 'Evite zonas bajas, lleve paraguas, conduzca con precaución.',
            'category': 'rain',
            'effective': '2026-10-23',
            'expires': '2026-10-24',
            'location': 'Tokyo',
            'source': 'WeatherAPI (detected)'
        },
        {
            'headline': 'Tormenta tropical en aproximación',
            'severity': 'high',
            'description': 'Tormenta tropical con vientos de 90 km/h. Posibles cortes de energía.',
            'instruction': 'Prepare suministros de emergencia, asegure ventanas, evacúe si es ordenado.',
            'category': 'storm',
            'effective': '2026-10-23',
            'expires': '2026-10-25',
            'location': 'Miami',
            'source': 'WeatherAPI'
        },
        {
            'headline': 'Ola de frío: -12°C',
            'severity': 'extreme',
            'description': 'Temperatura mínima de -12°C. Riesgo de hipotermia y congelación.',
            'instruction': 'Abríguese adecuadamente, mantenga su hogar calefaccionado, cuide a mascotas.',
            'category': 'temperature',
            'effective': '2026-10-23',
            'expires': '2026-10-26',
            'location': 'Moscow',
            'source': 'WeatherAPI (detected)'
        },
        {
            'headline': 'Nieve intensa prevista',
            'severity': 'moderate',
            'description': 'Probabilidad de nieve del 70%. Acumulación de 10-15 cm esperada.',
            'instruction': 'Use cadenas en neumáticos, abríguese, planee con anticipación.',
            'category': 'snow',
            'effective': '2026-10-24',
            'expires': '2026-10-25',
            'location': 'Toronto',
            'source': 'WeatherAPI (detected)'
        },
        {
            'headline': 'Alerta de calidad del aire',
            'severity': 'moderate',
            'description': 'Niveles de contaminación elevados. Personas sensibles deben limitar actividades al aire libre.',
            'instruction': 'Use mascarilla, mantenga ventanas cerradas, limite ejercicio intenso.',
            'category': 'air_quality',
            'effective': '2026-10-23',
            'expires': '2026-10-24',
            'location': 'Beijing',
            'source': 'WeatherAPI'
        },
        {
            'headline': 'Ola de calor: 38°C',
            'severity': 'high',
            'description': 'Temperatura máxima de 38°C. Índice UV extremo.',
            'instruction': 'Use protector solar, busque sombra, manténgase hidratado.',
            'category': 'temperature',
            'effective': '2026-10-23',
            'expires': '2026-10-24',
            'location': 'Sydney',
            'source': 'WeatherAPI (detected)'
        }
    ]

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    for alert in sample_alerts:
        cursor.execute('''
            INSERT INTO weather_alerts (headline, severity, description, instruction, category, effective, expires, location, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            alert['headline'],
            alert['severity'],
            alert['description'],
            alert['instruction'],
            alert['category'],
            alert['effective'],
            alert['expires'],
            alert['location'],
            alert['source']
        ))

    conn.commit()
    conn.close()
    print(f"✅ Se insertaron {len(sample_alerts)} alertas climáticas de ejemplo")


def init_db():
    """Inicializa la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Tabla de noticias
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT,
            source TEXT,
            date TEXT,
            impact_level TEXT,
            keywords TEXT
        )
    ''')

    # Tabla de alertas climáticas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            headline TEXT NOT NULL,
            severity TEXT,
            description TEXT,
            instruction TEXT,
            category TEXT,
            effective TEXT,
            expires TEXT,
            location TEXT NOT NULL,
            source TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Base de datos inicializada")


def clear_all_data():
    """Limpia todos los datos de la base de datos"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM news')
    cursor.execute('DELETE FROM weather_alerts')

    conn.commit()
    conn.close()
    print("🗑️  Se limpiaron todos los datos de la base de datos")


if __name__ == '__main__':
    print("🔄 Poblando base de datos con datos de ejemplo...\n")

    # Inicializar base de datos
    init_db()
    print()

    # Limpiar datos existentes
    clear_all_data()
    print()

    # Poblar datos
    populate_sample_news()
    populate_sample_alerts()

    print("\n✨ Base de datos poblada exitosamente!")
    print("📊 Ahora puedes ejecutar 'python3 app.py' para ver el dashboard con datos de ejemplo.")
