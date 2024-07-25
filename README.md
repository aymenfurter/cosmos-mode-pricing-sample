# Populate Cosmos DB Data

This script populates the model-pricing container.

## Prerequisites  

- Python 3.x
- `azure-cosmos` library
- `python-dotenv` library

## Installation

1. Clone the repository or download the `populate_data.py` script.
2. Install the required Python packages:
   ```bash
   pip install azure-cosmos python-dotenv
   ```

3. Create a `.env` file in the same directory as `populate_data.py` and populate it with your Cosmos DB configuration. You can use the `.env.sample` file as a template.

## Environment Variables

Create a `.env` file in the root directory and add the following variables:

```env
COSMOS_DB_ACCOUNT=cosmos-8234728934hdfs
DATABASE_NAME=ai-usage-db
CONTAINER_NAME=model-pricing
COSMOS_DB_KEY=<YOUR_COSMOS_DB_KEY>
```

Replace `<YOUR_COSMOS_DB_KEY>` with your actual Cosmos DB key.

## Usage

Run the script to reset and populate the container data:

```bash
python populate_data.py
```

This will delete all existing data in the specified container and insert the predefined data.