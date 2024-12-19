
pip install azure-ai-ml
pip install azure-identity
import logging

from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# Configure logging
logging.basicConfig(filename='logs/register_model.log', level=logging.INFO)
# Authenticate and initialize MLClient
# change  your credentials
#***********************************************************************
credential = DefaultAzureCredential()
SUBSCRIPTION="your subscription id"
RESOURCE_GROUP="gv-dp100-l9d092690c5d049baa1"
WS_NAME="mlw-dp100-l9d092690c5d049baa1"
#*********************************************************************
# Get a handle to the workspace
ml_client = MLClient(
    credential=credential,
    subscription_id=SUBSCRIPTION,
    resource_group_name=RESOURCE_GROUP,
    workspace_name=WS_NAME,
)
ml_client = MLClient.from_config(credential=credential)

# Define the model name and path
model_name = 'heart-prediction-pickle-model'

# Register the model as a custom model
model = ml_client.models.create_or_update(
    Model(name=model_name, path='./model', type=AssetTypes.CUSTOM_MODEL)
)

  logging.info("Model registered: {model.name} with version: {model.version}")
