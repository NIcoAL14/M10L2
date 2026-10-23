from flask import Flask, render_template, jsonify, request
import sqlite3
from datetime import datetime
from dotenv import load_dotenv
import os
import requests
import webbrowser
import socket

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
DB_NAME = 'climate_news.db'

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

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Dashboard con visualizaciones"""
    return render_template('dashboard.html')

@app.route('/map')
def world_map():
    """Mapa interactivo del mundo"""
    return render_template('map.html')

@app.route('/api/news')
def get_news():
    """API para obtener noticias"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM news ORDER BY date DESC LIMIT 20')
    news = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(news)

@app.route('/api/stats')
def get_stats():
    """API para obtener estadísticas"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT impact_level, COUNT(*) as count FROM news GROUP BY impact_level')
    stats = dict(cursor.fetchall())
    conn.close()
    return jsonify(stats)

@app.route('/api/weather-alerts')
def get_weather_alerts():
    """API para obtener alertas climáticas"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM weather_alerts
        WHERE DATE(effective) >= DATE('now', '-7 days')
        ORDER BY effective DESC
        LIMIT 50
    ''')
    alerts = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(alerts)

@app.route('/api/weather-alerts/stats')
def get_weather_alerts_stats():
    """API para obtener estadísticas de alertas climáticas"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT severity, COUNT(*) as count FROM weather_alerts GROUP BY severity')
    stats = dict(cursor.fetchall())
    conn.close()
    return jsonify(stats)

@app.route('/api/weather/current')
def get_current_weather():
    """API para obtener el clima actual por coordenadas o ciudad"""
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    city = request.args.get('city')

    api_key = os.getenv('WEATHER_API_KEY')

    if not api_key:
        return jsonify({'error': 'WeatherAPI key not configured'}), 500

    try:
        if lat and lon:
            # Usar coordenadas
            location = f"{lat},{lon}"
        elif city:
            # Usar nombre de ciudad
            location = city
        else:
            return jsonify({'error': 'Provide lat/lon or city parameter'}), 400

        url = f"http://api.weatherapi.com/v1/current.json"
        params = {
            'key': api_key,
            'q': location,
            'aqi': 'yes'  # Incluir calidad del aire
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        elif response.status_code == 400:
            # Ubicación no encontrada o inválida
            return jsonify({'error': 'Ubicación no encontrada. Intenta hacer clic en otra área.'}), 400
        elif response.status_code == 404:
            # Ubicación no encontrada
            return jsonify({'error': 'Ubicación no encontrada. Intenta hacer clic en una ciudad o área poblada.'}), 404
        else:
            return jsonify({'error': f'WeatherAPI error: {response.status_code}'}), response.status_code

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Tiempo de espera agotado. Intenta nuevamente.'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error de conexión: {str(e)}'}), 500

@app.route('/api/weather/forecast')
def get_weather_forecast():
    """API para obtener pronóstico del clima por coordenadas o ciudad"""
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    city = request.args.get('city')
    days = request.args.get('days', 3, type=int)

    api_key = os.getenv('WEATHER_API_KEY')

    if not api_key:
        return jsonify({'error': 'WeatherAPI key not configured'}), 500

    try:
        if lat and lon:
            location = f"{lat},{lon}"
        elif city:
            location = city
        else:
            return jsonify({'error': 'Provide lat/lon or city parameter'}), 400

        url = f"http://api.weatherapi.com/v1/forecast.json"
        params = {
            'key': api_key,
            'q': location,
            'days': min(days, 7),  # Máximo 7 días
            'aqi': 'yes'
        }

        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        elif response.status_code == 400:
            return jsonify({'error': 'Ubicación no encontrada para pronóstico.'}), 400
        elif response.status_code == 404:
            return jsonify({'error': 'Ubicación no encontrada para pronóstico.'}), 404
        else:
            return jsonify({'error': f'WeatherAPI error: {response.status_code}'}), response.status_code

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Tiempo de espera agotado. Intenta nuevamente.'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Error de conexión: {str(e)}'}), 500

def get_local_ip():
    """Obtiene la dirección IP local de la máquina"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

if __name__ == '__main__':
    import os

    init_db()

    # Obtener IP local
    local_ip = get_local_ip()
    port = 5001  # Cambiado de 5000 a 5001 para evitar conflicto con AirPlay

    # URL para acceder localmente (página principal)
    local_url = f"http://127.0.0.1:{port}/"
    # URL para que otros usuarios accedan desde la red (página principal)
    network_url = f"http://{local_ip}:{port}/"

    print("\n" + "="*60)
    print("🌍 ClimateNews AI - Servidor Iniciado")
    print("="*60)
    print(f"\n📍 Acceso local: {local_url}")
    print(f"🌐 Acceso desde la red: {network_url}")
    print(f"\n💡 Comparte la URL de red con tus compañeros para que accedan")
    print("="*60 + "\n")

    # Abrir navegador automáticamente solo una vez (no en reinicios de debug)
    if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
        webbrowser.open(local_url)

    # Ejecutar app en host='0.0.0.0' para aceptar conexiones de cualquier IP
    app.run(host='0.0.0.0', port=port, debug=True)
