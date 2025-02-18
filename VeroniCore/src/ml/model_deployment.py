# model_deployment.py
# This script manages the deployment of trained machine learning models into the VeroniCore system for real-time analysis and predictions.

import joblib
import os

class ModelDeploymentManager:
    def __init__(self, model_dir="VeroniCore/models"):
        self.model_dir = model_dir
        if not os.path.exists(model_dir):
            os.makedirs(model_dir)
        print(f"Model directory set to: {self.model_dir}")

    def deploy_model(self, model, model_name):
        model_path = os.path.join(self.model_dir, f"{model_name}.pkl")
        joblib.dump(model, model_path)
        print(f"Model '{model_name}' deployed successfully to {model_path}")
        return model_path

    def load_model(self, model_name):
        model_path = os.path.join(self.model_dir, f"{model_name}.pkl")
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            print(f"Model '{model_name}' loaded successfully from {model_path}")
            return model
        else:
            print(f"Model '{model_name}' not found at {model_path}")
            return None

    def list_deployed_models(self):
        models = [f for f in os.listdir(self.model_dir) if f.endswith('.pkl')]
        print("Deployed Models:")
        for model in models:
            print(f"- {model}")
        return models

if __name__ == "__main__":
    from sklearn.ensemble import RandomForestClassifier
    import numpy as np

    # Example usage of ModelDeploymentManager
    deployment_manager = ModelDeploymentManager()

    # Create and deploy a model
    X_train = np.random.rand(100, 10)  # 100 samples, 10 features
    y_train = np.random.randint(0, 2, 100)  # Binary labels

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    deployment_manager.deploy_model(model, "random_forest")

    # List deployed models
    deployment_manager.list_deployed_models()

    # Load the model
    loaded_model = deployment_manager.load_model("random_forest")
    