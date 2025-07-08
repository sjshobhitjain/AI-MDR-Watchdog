from parser import parse_log_file
from features import extract_features
from model import LogAnomalyModel

def run():
    logs = parse_log_file("logs/sample_auth.log")
    X = extract_features(logs)

    model = LogAnomalyModel()
    model.train(X)
    predictions = model.predict(X)

    for i, pred in enumerate(predictions):
        if pred == -1:
            print(f"⚠️ Anomaly: {logs[i]}")

if __name__ == "__main__":
    run()
