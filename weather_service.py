import requests
import os
from datetime import datetime
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

class WeatherAlertService:
    """Servicio para obtener alertas climáticas de WeatherAPI"""

    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')
        self.base_url = 'http://api.weatherapi.com/v1'

    def get_weather_alerts(self, location):
        """
        Obtiene alertas climáticas para una ubicación específica

        Args:
            location (str): Nombre de la ciudad o coordenadas (lat,lon)

        Returns:
            dict: Información de alertas climáticas o None si hay error
        """
        if not self.api_key:
            print("⚠️  Error: WEATHER_API_KEY no está configurada")
            return None

        try:
            url = f"{self.base_url}/forecast.json"
            params = {
                'key': self.api_key,
                'q': location,
                'days': 7,
                'alerts': 'yes'
            }

            response = requests.get(url, params=params, timeout=10)

            if response.status_code == 200:
                data = response.json()
                return self._parse_alerts(data, location)
            else:
                print(f"❌ Error en API Weather: {response.status_code}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Error de conexión: {e}")
            return None

    def get_alerts_multiple_locations(self, locations):
        """
        Obtiene alertas climáticas para múltiples ubicaciones

        Args:
            locations (list): Lista de nombres de ciudades o coordenadas

        Returns:
            list: Lista de alertas de todas las ubicaciones
        """
        all_alerts = []

        for location in locations:
            alert_data = self.get_weather_alerts(location)
            if alert_data:
                all_alerts.extend(alert_data)

        return all_alerts

    def _parse_alerts(self, data, location):
        """
        Parsea la respuesta de WeatherAPI para extraer alertas

        Args:
            data (dict): Respuesta JSON de WeatherAPI
            location (str): Ubicación consultada

        Returns:
            list: Lista de alertas procesadas
        """
        alerts = []

        # WeatherAPI puede incluir alertas en diferentes campos
        # Verificamos si hay alertas en la respuesta
        if 'alerts' in data and data['alerts']:
            for alert in data['alerts']['alert']:
                alerts.append({
                    'headline': alert.get('headline', 'Sin título'),
                    'severity': alert.get('severity', 'unknown'),
                    'description': alert.get('desc', ''),
                    'instruction': alert.get('instruction', ''),
                    'category': alert.get('category', 'general'),
                    'effective': alert.get('effective', ''),
                    'expires': alert.get('expires', ''),
                    'location': location,
                    'source': 'WeatherAPI'
                })

        # Si no hay alertas explícitas, verificamos condiciones extremas
        if not alerts and 'forecast' in data:
            alerts.extend(self._check_extreme_conditions(data, location))

        return alerts

    def _check_extreme_conditions(self, data, location):
        """
        Verifica condiciones climáticas extremas que podrían ser alertas

        Args:
            data (dict): Respuesta JSON de WeatherAPI
            location (str): Ubicación consultada

        Returns:
            list: Lista de alertas basadas en condiciones extremas
        """
        alerts = []
        forecast = data.get('forecast', {}).get('forecastday', [])

        for day in forecast:
            day_data = day.get('day', {})
            max_temp = day_data.get('maxtemp_c', 0)
            min_temp = day_data.get('mintemp_c', 0)
            max_wind = day_data.get('maxwind_kph', 0)
            daily_chance_of_rain = day_data.get('daily_chance_of_rain', 0)
            daily_chance_of_snow = day_data.get('daily_chance_of_snow', 0)

            date = day.get('date', '')

            # Alerta de calor extremo (más de 40°C)
            if max_temp > 40:
                alerts.append({
                    'headline': f'Ola de calor extrema: {max_temp}°C',
                    'severity': 'extreme',
                    'description': f'Temperatura máxima de {max_temp}°C. Riesgo de golpe de calor y deshidratación.',
                    'instruction': 'Manténgase hidratado, evite exposición al sol, use aire acondicionado.',
                    'category': 'temperature',
                    'effective': date,
                    'expires': date,
                    'location': location,
                    'source': 'WeatherAPI (detected)'
                })

            # Alerta de frío extremo (menos de -10°C)
            elif min_temp < -10:
                alerts.append({
                    'headline': f'Ola de frío extrema: {min_temp}°C',
                    'severity': 'extreme',
                    'description': f'Temperatura mínima de {min_temp}°C. Riesgo de hipotermia y congelación.',
                    'instruction': 'Abríguese adecuadamente, mantenga su hogar calefaccionado.',
                    'category': 'temperature',
                    'effective': date,
                    'expires': date,
                    'location': location,
                    'source': 'WeatherAPI (detected)'
                })

            # Alerta de viento fuerte (más de 60 km/h)
            if max_wind > 60:
                alerts.append({
                    'headline': f'Vientos fuertes: {max_wind} km/h',
                    'severity': 'high',
                    'description': f'Rachas de viento de hasta {max_wind} km/h. Riesgo de caída de árboles y daños estructurales.',
                    'instruction': 'Evite salir, asegure objetos sueltos, manténgase alejado de árboles.',
                    'category': 'wind',
                    'effective': date,
                    'expires': date,
                    'location': location,
                    'source': 'WeatherAPI (detected)'
                })

            # Alerta de lluvia intensa (más de 80% probabilidad)
            if daily_chance_of_rain > 80:
                alerts.append({
                    'headline': 'Lluvia intensa prevista',
                    'severity': 'moderate',
                    'description': f'Probabilidad de lluvia del {daily_chance_of_rain}%. Posibles inundaciones.',
                    'instruction': 'Evite zonas bajas, lleve paraguas, conduzca con precaución.',
                    'category': 'rain',
                    'effective': date,
                    'expires': date,
                    'location': location,
                    'source': 'WeatherAPI (detected)'
                })

            # Alerta de nieve (más de 50% probabilidad)
            if daily_chance_of_snow > 50:
                alerts.append({
                    'headline': 'Nieve prevista',
                    'severity': 'moderate',
                    'description': f'Probabilidad de nieve del {daily_chance_of_snow}%. Posibles interrupciones en transporte.',
                    'instruction': 'Use cadenas en neumáticos, abríguese, planee con anticipación.',
                    'category': 'snow',
                    'effective': date,
                    'expires': date,
                    'location': location,
                    'source': 'WeatherAPI (detected)'
                })

        return alerts


# Ciudades principales del mundo para monitorear
MAJOR_CITIES = [
    'New York',
    'London',
    'Tokyo',
    'Paris',
    'Sydney',
    'Moscow',
    'Beijing',
    'São Paulo',
    'Mumbai',
    'Mexico City',
    'Cairo',
    'Lagos',
    'Buenos Aires',
    'Istanbul',
    'Jakarta',
    'Seoul',
    'Toronto',
    'Dubai',
    'Singapore',
    'Los Angeles',
    'Madrid',
    'Rome',
    'Berlin',
    'Bangkok',
    'Hong Kong'
]


if __name__ == '__main__':
    # Prueba del servicio
    service = WeatherAlertService()

    print("🌍 Obteniendo alertas climáticas de ciudades principales...")
    alerts = service.get_alerts_multiple_locations(MAJOR_CITIES[:5])  # Prueba con 5 ciudades

    if alerts:
        print(f"\n✅ Se encontraron {len(alerts)} alertas:")
        for alert in alerts:
            print(f"\n📍 {alert['location']}")
            print(f"   {alert['headline']}")
            print(f"   Severidad: {alert['severity']}")
            print(f"   Fecha: {alert['effective']}")
    else:
        print("\nℹ️  No se encontraron alertas activas en este momento.")
