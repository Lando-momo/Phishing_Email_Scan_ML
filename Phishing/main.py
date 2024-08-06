from sklearn.tree import DecisionTreeClassifier
from joblib import load
from attrib import extract_features
from flask_cors import CORS


from joblib import load

# Specify the correct path to the saved model file
model_path = r"D:\Email_Guardian_ML-main\Email_Guardian_ML-main\python_server\phishing_detection\decision_tree_model.pkl"

# Load the saved model
classifier: DecisionTreeClassifier = load(model_path)
