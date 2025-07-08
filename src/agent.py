import time
from pathlib import Path
from model import LogAnomalyModel
from parser import parse_line
from features import extract_features

LOG_PATH = "logs/sample_auth.log"
model = LogAnomalyModel()

# Train once on historical data
def initialize_model():
    with open(LOG_PATH) as f:
        logs = [parse_line(line) for line in f if parse_line(line)]
    X = extract_features(logs)
    model.train(X)

# Monitor new entries
def monitor_live():
    with open(LOG_PATH) as f:
        f.seek(0, 2)  # Move to end of file
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            parsed = parse_line(line)
            if parsed:
                X_new = extract_features([parsed])
                pred = model.predict(X_new)[0]
                if pred == -1:
                    print(f"⚠️ Real-time anomaly detected: {parsed}")
