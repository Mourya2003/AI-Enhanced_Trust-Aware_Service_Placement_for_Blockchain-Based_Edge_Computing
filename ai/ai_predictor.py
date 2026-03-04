import numpy as np
from sklearn.ensemble import RandomForestClassifier

class ReliabilityPredictor:

    def __init__(self):

        X = np.array([
        [80,0.9,2],
        [70,0.85,3],
        [60,0.75,5],
        [90,0.95,1],
        [50,0.65,7],
        [85,0.92,2]
        ])

        y = np.array([0,0,1,0,1,0])

        self.model = RandomForestClassifier()
        self.model.fit(X,y)

    def predict(self,trust,success_rate,failures):

        data = [[trust,success_rate,failures]]

        return self.model.predict(data)[0]