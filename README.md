# HRIS-scripts
HRIS Migration Scripts

# HRIS Migration Scripts

This mini toolkit includes scripts for migrating employee records from a legacy HR platform to a modern API-based HRIS.

## Files
- `export_legacy_employees.py` – Simulates export from a legacy system
- `transform_to_new_format.py` – Transforms CSV data to JSON for the new system
- `import_to_new_hris.py` – Imports JSON data into the new HRIS via API

## Usage
```bash
python export_legacy_employees.py
python transform_to_new_format.py
python import_to_new_hris.py

    Note: Update the API endpoint and token in import_to_new_hris.py before running in production.

