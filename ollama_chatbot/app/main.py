from flask import Flask, request, jsonify
import requests
import threading
import time
import sys

app = Flask(__name__)

# Service Discovery URL
REGISTRAR_URL = 'http://localhost:5000/service-discovery'
SERVICE_NAME = sys.argv[1]
SERVICE_PORT = sys.argv[2]
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3.2"

def register_service():
    """Registers this microservice with the service discovery system"""
    try:
        requests.post(
            f"{REGISTRAR_URL}/register",
            json={'name': SERVICE_NAME, 'address': f'http://localhost:{SERVICE_PORT}'}
        )
    except requests.exceptions.RequestException:
        pass

def send_heartbeat():
    """Sends a heartbeat every 2 minutes"""
    while True:
        try:
            requests.post(f"{REGISTRAR_URL}/heartbeat", json={'name': SERVICE_NAME})
        except requests.exceptions.RequestException:
            pass
        time.sleep(120)

@app.route('/process', methods=['POST'])
def process_request():
    """Handles AI processing using Ollama"""
    data = request.get_json()
    ollama_response = requests.post(
        OLLAMA_URL,
        json={'model': MODEL_NAME, 'prompt': data['prompt'], 'stream': False}
    )

    if ollama_response.status_code == 200:
        return jsonify({'from': SERVICE_NAME, 'response': ollama_response.json().get('response')})
    
    return jsonify({'error': 'Ollama processing failed'}), 500

if __name__ == '__main__':
    register_service()
    threading.Thread(target=send_heartbeat, daemon=True).start()
    app.run(host='0.0.0.0', port=SERVICE_PORT)
