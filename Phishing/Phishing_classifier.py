import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

def main():
    file_path = r'D:\Email_Guardian_ML-main\Email_Guardian_ML-main\python_server\phishing_detection\dataset.csv'
    
    # Load dataset
    training_data = np.genfromtxt(file_path, delimiter=',', dtype=np.int32)
    inputs = training_data[:, :-1]
    outputs = training_data[:, -1]

    # Split data into training and testing sets
    training_inputs = inputs[:2000]
    training_outputs = outputs[:2000]
    testing_inputs = inputs[2000:]
    testing_outputs = outputs[2000:]

    # Initialize and train DecisionTreeClassifier
    classifier = DecisionTreeClassifier()
    classifier.fit(training_inputs, training_outputs)

    
    # Save trained model to pickle file
    with open('decision_tree_model.pkl', 'wb') as model_file:
        pickle.dump(classifier, model_file)

    # Evaluate model accuracy
    predictions = classifier.predict(testing_inputs)
    accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
    print(f"Model Accuracy: {accuracy}%")

if __name__ == "__main__":
    main()
