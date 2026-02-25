# Microservices Service Discovery using Consul & Docker

A production-style microservices project demonstrating Service Discovery using HashiCorp Consul, built with Flask, containerized using Docker, and orchestrated via Docker Compose.

This project simulates a distributed system where multiple services dynamically register themselves with Consul and are accessed through an API Gateway.

📌 Project Overview

This system consists of:
Service A (Port 5001)
Service B (Port 5002)
Service C (Port 5003)
Consul (Service Registry – Port 8500)
API Gateway (Port 8000)
Each service:

Registers itself dynamically to Consul
Provides a health check endpoint
Can be discovered via Consul
Is routed through API Gateway

🛠️ Tech Stack

Python 3
Docker
Flask
Docker Compose
Requests

Docker

Docker Compose
