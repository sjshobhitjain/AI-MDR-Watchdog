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

## 🏃 How to Run

1. Clone the repo
2. Install dependencies:
