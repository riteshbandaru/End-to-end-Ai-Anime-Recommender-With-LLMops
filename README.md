# 🎌 AI Anime Recommender with LLMOps 🚀

This project is an **AI-powered Anime Recommendation System** built using **LangChain**, **LLMs**, and **Vector Databases** — deployed end-to-end using **Docker**, **Kubernetes**, and **Minikube** on a **GCP Virtual Machine (VM)**.

---

## 📁 Project Structure

Ai_Anime_Recommender/
│
├── app/ # Streamlit frontend
├── chroma_db/ # Vector DB files (Chroma)
├── config/ # Config files
├── data/ # Raw & processed data
├── pipeline/ # Data pipeline for prediction & building
├── src/ # Core logic (recommender, vector store, prompt template, etc.)
├── utils/ # Helper utilities
├── Dockerfile # Docker container config
├── llmops-k8s.yaml # Kubernetes deployment/service config
├── requirements.txt # Python dependencies
└── setup.py # Python setup for pip install -e .



---

## ⚙️ Features

- 🔎 Semantic search with vector embeddings
- 🧠 LLM-powered anime recommendation
- 🐳 Docker containerization
- ☸️ Kubernetes deployment using Minikube
- ☁️ Hosted on a Google Cloud VM

---

## 🖥️ Setup on GCP VM (Ubuntu/Linux)

### 1. ✅ Enable Docker

```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
---
## 2. 🔍 Verify Docker Installation
bash
Copy
Edit
systemctl status docker
docker ps
docker ps -a
You should see the Docker daemon running.

### 3. 🛠️ Install Minikube & kubectl

#### a. Install Minikube

Go to [Minikube installation page](https://minikube.sigs.k8s.io/docs/start/ ), choose:

- **OS:** Linux  
- **Architecture:** x86  
- **Download the binary**

Then run the following commands:

```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 
sudo install minikube-linux-amd64 /usr/local/bin/minikube
b. Start Minikube Cluster
bash
Copy
Edit
minikube start
c. Install kubectl
bash
Copy
Edit
sudo snap install kubectl --classic
kubectl version --client
4. 🔐 Setup GitHub & Push Code (optional)
```bash

git config --global user.email "your-email@gmail.com"
git config --global user.name "your-username"

git add .
git commit -m "deploy"
git push origin main
📦 5. Docker Build and Kubernetes Deployment
🐳 Point Docker to Minikube:
bash
Copy
Edit
eval $(minikube docker-env)
🔨 Build Docker Image:
bash
Copy
Edit
docker build -t llmops-app:latest .
🔑 Add Environment Secrets (for APIs):
bash
Copy
Edit
kubectl create secret generic llmops-secrets \
  --from-literal=GROQ_API_KEY="your_key_here" \
  --from-literal=HUGGINGFACEHUB_API_TOKEN="your_token_here"
🚀 Deploy App with Kubernetes
bash
Copy
Edit
kubectl apply -f llmops-k8s.yaml
🧠 Check Kubernetes Status
bash
Copy
Edit
kubectl get pods
kubectl get svc
minikube status
kubectl cluster-info
🌐 Access the App Publicly
Minikube does not expose LoadBalancer services by default. Use a tunnel + port-forward.

Terminal 1 – Create Tunnel:
bash
Copy
Edit
minikube tunnel
Terminal 2 – Forward Port to Host:
bash
Copy
Edit
kubectl port-forward svc/llmops-service 8501:80 --address 0.0.0.0
Now access it at:

bash
Copy
Edit
http://<your-vm-external-ip>:8501
🧾 Kubernetes File Explained (llmops-k8s.yaml)
yaml
Copy
Edit
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llmops-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: llmops
  template:
    metadata:
      labels:
        app: llmops
    spec:
      containers:
        - name: llmops-container
          image: llmops-app:latest
          ports:
            - containerPort: 8501
          envFrom:
            - secretRef:
                name: llmops-secrets

---
apiVersion: v1
kind: Service
metadata:
  name: llmops-service
spec:
  type: LoadBalancer
  selector:
    app: llmops
  ports:
    - port: 80
      targetPort: 8501
🎯 Final Output
You will get a running AI Anime Recommendation App powered by LLMs and served through Kubernetes on GCP:

📍 URL: http://<your-external-vm-ip>:8501

📌 Notes
Keep tunnel & port-forwarding terminals running for access.

You can later shift from Minikube to real Kubernetes clusters (GKE, EKS, AKS).

Ensure your VM firewall rules allow ingress on port 8501.

📬 Contact
For help, reach out to: riteshbandaru27@gmail.com
GitHub: riteshbandaru

