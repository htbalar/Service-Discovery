# 🧠 Ollama Chatbot Microservice with Service Discovery

A **microservices-based chatbot** using **Flask** and **Ollama**, integrated with a **dynamic service discovery system** to enable seamless communication between services.

---

## 📌 Features
- ✅ **Service Discovery** - Services dynamically register, send heartbeats, and communicate without hardcoded addresses.
- ✅ **Ollama AI Processing** - Chatbot uses **Llama 3.2** for AI-generated responses.
- ✅ **Automatic Cleanup** - Inactive services are removed after **5 minutes**.
- ✅ **Message Forwarding** - Microservices can send messages to each other.

---

## 📂 Project Structure

```
 Service-Discovery/         # Service discovery system
│   ├── app/
│   │   ├── controllers/
│   │   │   ├── service_discovery_controller.py  # API endpoints
│   │   ├── services/
│   │   │   ├── service_discovery_service.py  # Core logic (service registry)
│   │   ├── main.py  # Runs the service discovery system
│   ├── requirements.txt
│   ├── venv/
│
│── ollama_chatbot/            # AI Chatbot microservice
│   ├── app/
│   │   ├── main.py  # Handles registration, AI processing
│   ├── requirements.txt
│   ├── venv/
│
│── README.md
```

---

## 🛠️ Pre-requisites

### 🔹 1. Install Ollama
Ollama is required for AI processing. Install it using the following steps:

**Linux & macOS:**
```sh
curl -fsSL https://ollama.ai/install.sh | sh
```

**Windows:**
Download and install from [Ollama Official Website](https://ollama.ai/).

Ensure Ollama is running:
```sh
ollama serve &
```

### 🔹 2. Install Python & Virtual Environment
Ensure Python 3.8+ is installed:
```sh
python --version
```
If not installed, download it from [Python Official Website](https://www.python.org/downloads/).

---

## 🛠️ Installation & Setup

### 🔹 1. Clone the Repository
```sh
git clone https://github.com/htbalar/Service-Discovery.git
cd Service-Discovery
```

### 🔹 2. Install Dependencies

For **Service Discovery**:
```sh
cd Service-Discovery
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
deactivate
cd ..
```

For **Ollama Chatbot**:
```sh
cd ollama_chatbot
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
deactivate
cd ..
```

---

## 🚀 Running the Microservices

### 1️⃣ **Start the Service Discovery System** (Runs on port **5000**)
```sh
cd Service-Discovery
source venv/bin/activate
python app/main.py
```

### 2️⃣ **Start the Ollama Chatbot Microservice** (Runs on port **5001**)
```sh
cd ollama_chatbot
source venv/bin/activate
python app/main.py ollama_chatbot 5001
```

---

## 🧪 Testing API Calls

### ✅ **Check Registered Services**
```sh
curl -X GET http://localhost:5000/service-discovery/services
```

### ✅ **Send a Prompt to the Chatbot**
```sh
curl -X POST http://localhost:5001/process \
     -H "Content-Type: application/json" \
     -d '{"prompt": "What is AI?"}'
```

---

## 🔄 Stopping the Services

To **stop** all running services, press `CTRL + C` in each terminal.

---

## 🎯 Summary

| **Task**  | **Command**  |
|-------------------|-------------|
| Install dependencies  | `pip install -r requirements.txt`  |
| Run Service Discovery | `python app/main.py` (Port **5000**) |
| Run Ollama Chatbot | `python app/main.py ollama_chatbot 5001` (Port **5001**) |
| Get Services List | `curl -X GET http://localhost:5000/service-discovery/services` |
| Forward Message | `curl -X POST http://localhost:5000/service-discovery/forward` |
| Stop Everything | `CTRL + C`  |

---

## 📝 Contributing

1️⃣ **Fork the repository**
2️⃣ **Create a feature branch** (`git checkout -b feature-name`)
3️⃣ **Commit your changes** (`git commit -m "Added new feature"`)
4️⃣ **Push to GitHub** (`git push origin feature-name`)
5️⃣ **Create a Pull Request (PR)** 🚀

---
