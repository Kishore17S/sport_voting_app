# 🗳️ Favorite Sport Voting App

A simple Flask web application that allows users to vote for their favorite sport (🏏 Cricket or ⚽ Football). After voting, a "Voted successfully!" message is displayed. No data is stored.

---

## 🚀 Features

- Vote for your favorite sport: Cricket or Football
- Displays a simple confirmation message
- Lightweight and easy to deploy

---

## 🛠️ Tech Stack

- Python (Flask)
- HTML + CSS
- JavaScript
- ✅ Deployed on OpenShift Sandbox

---

## 📂 Folder Structure
project/ ├── app.py ├── frontend/ │ ├── index.html │ └── style.css └── README.md


---

## ▶️ Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/sport-voting-app.git
cd sport-voting-app

### 2. Install Flask

     pip install flask

### 3. Run the App

    python app.py

### 4. Access the App

Open your browser at: http://localhost:8080


🌐 Deployment on OpenShift Sandbox
📌 Prerequisites
OpenShift account with Developer Sandbox enabled
oc CLI tool installed and authenticated

🧩 Steps to Deploy

1.Create a new project in OpenShift
oc new-project flask-voting-app

2.Create a new app from Python image
oc new-app python:3.9~https://github.com/yourusername/sport-voting-app

3.Expose the service to create a public URL
oc expose svc/sport-voting-app

4.Find the route
oc get route

📄 License
MIT License – feel free to use and modify.


🙌 Acknowledgements
Deployed using OpenShift Developer Sandbox 🚀
Built with ❤️ using Flask & minimal frontend magic ✨

---

Let me know your GitHub repo link or the OpenShift route, and I can plug that in too for a polished final version!



