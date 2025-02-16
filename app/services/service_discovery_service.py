import time
import threading
import requests
from flask import jsonify
from datetime import datetime

services = {}
lock = threading.Lock()

HEARTBEAT_TIMEOUT = 300  # 5 minutes

def register_service(data):
    """Registers a microservice with its name and address"""
    service_name = data.get("name")
    service_address = data.get("address")

    if not service_name or not service_address:
        return jsonify({"error": "Service name and address required"}), 400

    with lock:
        services[service_name] = {"address": service_address, "last_heartbeat": datetime.now().timestamp()}
    
    return jsonify({"message": "Service registered successfully"}), 200

def heartbeat_check(data):
    """Updates the last heartbeat timestamp of a microservice"""
    service_name = data.get("name")

    with lock:
        if service_name in services:
            services[service_name]["last_heartbeat"] = datetime.now().timestamp()
            return jsonify({"message": "Heartbeat updated"}), 200
        else:
            return jsonify({"error": "Service not registered"}), 404

def list_services():
    """Returns all registered services"""
    with lock:
        return jsonify([{"name": k, "address": v["address"]} for k, v in services.items()])

def forward_message(data):
    """Forwards a message to another service"""
    from_service = data.get("from")
    to_service = data.get("to")
    prompt = data.get("prompt")

    if not to_service or not prompt:
        return jsonify({"error": "Target service and prompt required"}), 400

    with lock:
        target = services.get(to_service)
    
    if not target:
        return jsonify({"error": "Service not found"}), 404

    try:
        response = requests.post(
            f"{target['address']}/process",
            json={'from': from_service, 'prompt': prompt}
        )
        return response.json()
    except requests.exceptions.RequestException:
        return jsonify({'error': 'Failed to forward message'}), 500

def cleanup_expired_services():
    """Removes services that haven't sent a heartbeat in 5 minutes"""
    while True:
        time.sleep(60)
        current_time = datetime.now().timestamp()
        with lock:
            expired = [name for name, svc in services.items() if current_time - svc['last_heartbeat'] > HEARTBEAT_TIMEOUT]
            for name in expired:
                del services[name]

cleanup_thread = threading.Thread(target=cleanup_expired_services, daemon=True)
cleanup_thread.start()
