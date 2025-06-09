import requests
import json

API_ENDPOINT = "https://api.newhris.com/v1/employees"
API_KEY = "your-api-key-here"

def import_data(json_file):
    with open(json_file, 'r') as infile:
        employees = json.load(infile)
    
    for emp in employees:
        response = requests.post(
            API_ENDPOINT,
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json=emp
        )
        if response.status_code == 201:
            print(f"✅ Created employee {emp['fullName']}")
        else:
            print(f"❌ Failed to create {emp['fullName']}: {response.text}")

if __name__ == '__main__':
    import_data('new_hris_format.json')
