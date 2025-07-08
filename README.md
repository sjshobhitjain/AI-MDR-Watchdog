# AI-MDR-Watchdog

AI-enhanced MDR project that detects Linux threats using unsupervised ML.

## 🔍 What It Detects

- Abnormal SUDO commands
- Unknown user activity
- Suspicious software installs
- Launching unexpected tools

## 🧠 How It Works

- Parses Linux logs
- Extracts behavior features (user, command type)
- Trains Isolation Forest on normal behavior
- Flags outliers as anomalies

## 👮(V2 update) MDR Agent Mode 

Run the tool as a continuous watchdog:

```bash
python src/agent.py
```

## Add a CLI to run it as python src/agent.py --live

Or turn it into a background service:

Systemd service (Linux daemon)

Flask FastAPI microservice (expose REST API to trigger analysis)

