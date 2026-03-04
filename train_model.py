import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

# load dataset
df = pd.read_csv("datasets/node_dataset.csv")

X = df.drop("failure_risk", axis=1)
y = df["failure_risk"]

# split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# train model
model = RandomForestClassifier(n_estimators=100)
model.fit(X_train, y_train)

# predictions
pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)

print("Model Accuracy:", accuracy)

# confusion matrix
cm = confusion_matrix(y_test, pred)

plt.figure(figsize=(5,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")

# feature importance
importances = model.feature_importances_

plt.figure(figsize=(6,4))
sns.barplot(x=importances, y=X.columns)
plt.title("Feature Importance")
plt.savefig("feature_importance.png")

print("Graphs saved:")
print("confusion_matrix.png")
print("feature_importance.png")