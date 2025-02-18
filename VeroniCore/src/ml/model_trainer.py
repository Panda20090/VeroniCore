# model_trainer.py
# This script handles the training of machine learning models using data collected from the system and user interactions.

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ModelTrainer:
    def __init__(self, model, data, labels):
        self.model = model
        self.data = data
        self.labels = labels

    def prepare_data(self, test_size=0.2, random_state=42):
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.data, self.labels, test_size=test_size, random_state=random_state
        )
        print(f"Data prepared with {test_size*100}% for testing.")

    def train_model(self):
        self.model.fit(self.X_train, self.y_train)
        print("Model training completed.")

    def evaluate_model(self):
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        print(f"Model accuracy: {accuracy*100:.2f}%")
        return accuracy

if __name__ == "__main__":
    from sklearn.ensemble import RandomForestClassifier

    # Example usage of ModelTrainer
    # Generate some example data
    example_data = np.random.rand(100, 10)  # 100 samples, 10 features
    example_labels = np.random.randint(0, 2, 100)  # Binary labels

    # Initialize the model
    model = RandomForestClassifier()

    # Create the ModelTrainer instance
    trainer = ModelTrainer(model, example_data, example_labels)

    # Prepare data
    trainer.prepare_data()

    # Train the model
    trainer.train_model()

    # Evaluate the model
    trainer.evaluate_model()
    