from flask import Blueprint, request, jsonify
from services.service_discovery_service import (
    register_service, list_services, forward_message, heartbeat_check
)

service_discovery_ns = Blueprint("service_discovery", __name__)

@service_discovery_ns.route("/register", methods=["POST"])
def register():
    return register_service(request.json)

@service_discovery_ns.route("/services", methods=["GET"])
def get_services():
    return list_services()

@service_discovery_ns.route("/forward", methods=["POST"])
def forward():
    return forward_message(request.json)

@service_discovery_ns.route("/heartbeat", methods=["POST"])
def heartbeat():
    return heartbeat_check(request.json)
