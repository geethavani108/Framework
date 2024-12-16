import joblib
from azureml.core import Workspace, Model

def deploy_model(model_file):
    # Load Azure ML workspace
    ws = Workspace.from_config()
    
    # Register the model
    model = joblib.load(model_file)
    model = Model.register(workspace=ws, model_path=model_file, model_name='predictive_maintenance_model')
    print("Model registered: ", model.name)

if __name__ == "__main__":
    deploy_model('models/model.pkl')
