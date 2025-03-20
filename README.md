# 🧠 Ollama Microservice with Dynamic Service Discovery

A **Flask-based microservice architecture** using **Ollama (Llama 3.2)** for AI processing with **Service Discovery** to enable seamless communication between multiple services.

---

## 📌 Features
- ✅ **Service Registration**
- ✅ **Heartbeat Mechanism (Every 2 Minutes)**
- ✅ **Automatic Cleanup of Inactive Services (5 Minutes)**
- ✅ **Message Forwarding Between Microservices**

---

## 🛠️ Pre-requisites

1️⃣ Install **Ollama**:
```sh
curl -fsSL https://ollama.ai/install.sh | sh
```

2️⃣ Install **Python 3.8+** and create virtual environments for both **Service Discovery** and **Ollama Microservice**.

---

## 📂 Project Structure

```
 Service-Discovery/
│   ├── app/
│   │   ├── controllers/
│   │   │   ├── service_discovery_controller.py
│   │   ├── services/
│   │   │   ├── service_discovery_service.py
│   │   ├── main.py
│   ├── requirements.txt
│   ├── venv/
│
│── ollama_chatbot/
│   ├── app/
│   │   ├── main.py
│   ├── requirements.txt
│   ├── venv/
│
│── README.md
```

---

## ✅ Installation

### 🔹 Step 1: Clone the Repository
```sh
git clone https://github.com/htbalar/Service-Discovery.git
cd Service-Discovery
```

### 🔹 Step 2: Install Dependencies

For **Service Discovery**:
```sh
cd Service-Discovery
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

For **Ollama Microservice**:
```sh
cd Service-Discovery/ollama_chatbot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🚀 Running the Services

### 1️⃣ Run Service Discovery on Machine 1
```sh
cd Service-Discovery
venv\Scripts\activate
python app/main.py
```

### 2️⃣ Run Ollama Microservice on Machine 2
When starting the Ollama service, you need to provide a service name and port number as arguments.
```sh
python app/main.py <service_name> <port>
```
For example:
```sh
cd ollama_chatbot
venv\Scripts\activate
python app/main.py ollama_service_1 6000
```
- ollama_service_1: This is the unique name for the service.
- 6000: This is the port number the service will run on.

### 3️⃣ Run Ollama Microservice on Machine 3
For Machine 3, use a different name and port number, like this:
```sh
cd ollama_chatbot
venv\Scripts\activate
python app/main.py ollama_service_2 6001
```
**⚠️ Important Note**:

- Ensure all machines are in the same network.
- The Service Discovery IP address should be replaced in main.py file of Ollama service.

In `main.py`, update this line:
```sh
REGISTRAR_URL = 'http://localhost:5000/service-discovery'
```
Replace `<localhost>` and `5000` with the actual IP address and Port of the machine running the service discovery system.

---

## 🛠️ API Endpoints

### ✅ **Register a Service**
This endpoint allows a microservice to register itself with the Service Discovery system. This is essential for communication between different services.

**Example Command:**
```sh
curl -X POST http://<ServiceDiscovery_IP>:5000/service-discovery/register \
     -H "Content-Type: application/json" \
     -d '{"name": "ollama_service_1", "address": "http://<Machine_1_IP>:6000"}'
```
- Replace `<ServiceDiscovery_IP>` with the IP address of the machine running the Service Discovery system.
- Replace `<Machine_1_IP>` with the IP of the machine running the first Ollama microservice.
- Ensure that **both machines are on the same network** (e.g., connected to the same Wi-Fi or LAN).

### ✅ **Get All Registered Services**
This endpoint fetches a list of all active services registered with the Service Discovery system.

**Example Command:**
```sh
curl -X GET http://<ServiceDiscovery_IP>:5000/service-discovery/services
```
- This helps to verify if all services are successfully registered.

### ✅ **Send Message to Another Service**
This endpoint allows one service to forward a message to another registered service.

**Example Command:**
```sh
curl -X POST http://<ServiceDiscovery_IP>:5000/service-discovery/forward \
     -H "Content-Type: application/json" \
     -d '{"from": "ollama_service_1", "to": "ollama_service_2", "prompt": "What is AI?"}'
```
- In this example, `ollama_service_1` sends a message to `ollama_service_2`.
- Replace the service names as per your setup.

If you're running this system on two different laptops or servers, make sure:
1. Both machines are connected to the same Wi-Fi or LAN network.
2. Use the actual local IP addresses (e.g., `192.168.x.x`) instead of placeholders.
3. Ensure the Service Discovery system is running on one machine (e.g., Machine 3) to act as the central hub for communication.

---

## ✅ Heartbeat Check (Every 2 Minutes Automatically)

Each Ollama service will send a heartbeat every **2 minutes**, and if a service fails to send a heartbeat for **5 minutes**, it will be automatically removed from the Service Discovery registry.

---


## 📝 Contributing

1️⃣ Fork the repo
2️⃣ Create a feature branch (`git checkout -b feature-name`)
3️⃣ Commit changes (`git commit -m "Added new feature"`)
4️⃣ Push to GitHub (`git push origin feature-name`)
5️⃣ Open a Pull Request 🚀

---

