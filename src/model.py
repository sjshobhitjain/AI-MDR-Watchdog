from sklearn.ensemble import IsolationForest

class LogAnomalyModel:
    def __init__(self):
        self.model = IsolationForest(contamination=0.1, random_state=42)

    def train(self, features):
        self.model.fit(features)

    def predict(self, features):
        return self.model.predict(features)

    def score(self, features):
        return self.model.decision_function(features)
