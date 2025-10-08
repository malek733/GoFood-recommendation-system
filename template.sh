#!/bin/bash

# === GoFood AI Project Template ===

# Root directory


# Root files
touch .env requirements.txt main.py

# src structure
mkdir -p src/{config,data,models,agents,api,utils}
touch src/__init__.py

# Config
touch src/config/__init__.py src/config/supabase_client.py

# Data
touch src/data/__init__.py src/data/fetch_data.py src/data/preprocessing.py

# Models
touch src/models/__init__.py src/models/{recommender.py,embeddings.py,train_model.py}

# Agents
touch src/agents/__init__.py src/agents/{chatbot_agent.py,manager_agent.py,tools.py}

# API
touch src/api/__init__.py src/api/routes.py

# Utils
touch src/utils/__init__.py src/utils/{output_parser.py,logger.py}

# Notebooks
mkdir -p notebooks
touch notebooks/data_exploration.ipynb

# Write default placeholders
echo "# GoFood AI Project" > README.md
echo "# FastAPI entry point" > main.py
echo "# Add environment variables here" > .env
echo "# Python dependencies" > requirements.txt
echo "from supabase import create_client" > src/config/supabase_client.py

echo "✅ GoFood AI project structure created successfully!"
