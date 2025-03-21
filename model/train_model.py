from sklearn.linear_model import LogisticRegression
import joblib

# Train dummy model
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, y)

# Save it
joblib.dump(model, "model/model.pkl")
