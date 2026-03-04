import numpy as np
from sklearn.ensemble import RandomForestClassifier


class ReliabilityPredictor:

    def __init__(self):

        # training dataset
        # features = [trust_score, success_rate, failures]

        X = np.array([
            [80, 0.9, 2],
            [75, 0.88, 3],
            [60, 0.7, 6],
            [90, 0.95, 1],
            [55, 0.65, 8],
            [85, 0.92, 2],
            [70, 0.82, 4],
            [50, 0.6, 10]
        ])

        # 0 = reliable
        # 1 = failure

        y = np.array([0,0,1,0,1,0,1,1])

        self.model = RandomForestClassifier()

        self.model.fit(X, y)


    def predict(self, trust, success_rate, failures):

        data = [[trust, success_rate, failures]]

        prediction = self.model.predict(data)[0]

        return prediction