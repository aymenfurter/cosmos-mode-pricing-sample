import os
from azure.cosmos import CosmosClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configuration
COSMOS_DB_ACCOUNT = os.getenv('COSMOS_DB_ACCOUNT')
DATABASE_NAME = os.getenv('DATABASE_NAME')
CONTAINER_NAME = os.getenv('CONTAINER_NAME')
COSMOS_DB_KEY = os.getenv('COSMOS_DB_KEY')

# Data to populate
data_to_insert = [
    {
        "id": "1",
        "CostPerInputUnit": 0.0001,
        "CostPerOutputUnit": 0,
        "CostUnit": 1000,
        "Currency": "USD",
        "isActive": True,
        "model": "ada",
        "region": "ALL",
        "BaseCost": 0,
        "CalculationMethod": "tokens",
        "deploymentName": "embedding"
    },
    {
        "id": "2",
        "CostPerInputUnit": 0.0015,
        "CostPerOutputUnit": 0.002,
        "CostUnit": 1000,
        "Currency": "USD",
        "isActive": True,
        "model": "gpt-35-turbo",
        "region": "ALL",
        "BaseCost": 0,
        "CalculationMethod": "tokens",
        "deploymentName": "chat"
    },
    {
        "id": "3",
        "CostPerInputUnit": 0.03,
        "CostPerOutputUnit": 0.06,
        "CostUnit": 1000,
        "Currency": "USD",
        "isActive": True,
        "model": "gpt-4",
        "region": "ALL",
        "BaseCost": 0,
        "CalculationMethod": "tokens",
        "deploymentName": "gpt-4"
    },
    {
        "id": "4",
        "CostPerInputUnit": 0.005,
        "CostPerOutputUnit": 0.015,
        "CostUnit": 1000,
        "Currency": "USD",
        "isActive": True,
        "model": "gpt-4o",
        "region": "ALL",
        "BaseCost": 0,
        "CalculationMethod": "tokens",
        "deploymentName": "gpt-4o"
    },
    {
        "id": "5",
        "CostPerInputUnit": 4,
        "CostPerOutputUnit": 0,
        "CostUnit": 100,
        "Currency": "USD",
        "isActive": True,
        "model": "dall-e-3",
        "region": "ALL",
        "BaseCost": 0,
        "CalculationMethod": "tokens",
        "deploymentName": "dall-e-3"
    },
    {
        "id": "6",
        "CostPerInputUnit": 0,
        "CostPerOutputUnit": 1,
        "CostUnit": 1,
        "Currency": "USD",
        "isActive": True,
        "model": "ai-search",
        "region": "ALL",
        "BaseCost": 590,
        "CalculationMethod": "percentage",
        "deploymentName": "ai-search-business"
    }
]

# Initialize the Cosmos client
client = CosmosClient(f'https://{COSMOS_DB_ACCOUNT}.documents.azure.com:443/', COSMOS_DB_KEY)
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# Insert or update data
for item in data_to_insert:
    container.upsert_item(body=item)

print("Container data reset and populated successfully.")
