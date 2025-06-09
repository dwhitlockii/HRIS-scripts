import os
import json
import logging
import time
import requests
from typing import List
from pydantic import BaseModel, Field, ValidationError
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# API configuration
API_URL = os.getenv("HRIS_API_URL", "https://api.newhris.com/v1/employees")
API_KEY = os.getenv("HRIS_API_KEY", "your-token")

# Pydantic schema
class Compensation(BaseModel):
    baseSalary: float
    currency: str = "USD"

class Employee(BaseModel):
    employeeId: str
    fullName: str
    startDate: str
    compensation: Compensation

# Read data and validate
def load_employees(json_path: str) -> List[Employee]:
    with open(json_path, 'r') as file:
        raw_data = json.load(file)
    validated = []
    for entry in raw_data:
        try:
            validated.append(Employee(**entry))
        except ValidationError as e:
            logging.error(f"Validation failed for entry: {entry} – {e}")
    return validated

# Upload in chunks with retry logic
def upload_employees(employees: List[Employee], batch_size: int = 10):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    for i in range(0, len(employees), batch_size):
        chunk = employees[i:i+batch_size]
        payload = [e.dict() for e in chunk]

        for attempt in range(3):
            try:
                response = requests.post(API_URL, headers=headers, json=payload, timeout=10)
                if response.status_code == 201:
                    logging.info(f"✅ Uploaded batch {i // batch_size + 1}")
                    break
                else:
                    logging.warning(f"⚠️ Attempt {attempt+1}: {response.status_code} – {response.text}")
            except requests.RequestException as e:
                logging.error(f"❌ Network error on attempt {attempt+1}: {e}")
            time.sleep(2 ** attempt)  # exponential backoff

# Entrypoint
if __name__ == '__main__':
    path = "new_hris_format.json"
    logging.info("🚀 Starting employee data migration")
    employees = load_employees(path)
    if not employees:
        logging.warning("No valid employees to migrate.")
        exit(1)
    upload_employees(employees)
    logging.info("🎉 Migration complete.")
