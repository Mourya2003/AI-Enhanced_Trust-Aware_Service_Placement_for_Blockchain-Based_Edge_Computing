import joblib
import numpy as np


class ReliabilityPredictor:

    def __init__(self):

        # Load trained model
        self.model = joblib.load(
            "ai/trained_model.pkl"
        )

    def predict(
        self,
        trust,
        success_rate,
        failures
    ):

        data = np.array([[
            trust,
            success_rate,
            failures,
            50,   # latency placeholder
            50,   # cpu placeholder
            50    # memory placeholder
        ]])

        prediction = self.model.predict(data)[0]

        return prediction