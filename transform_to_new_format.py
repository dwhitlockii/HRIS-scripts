import csv
import json

def transform_csv_to_json(csv_file, json_file):
    with open(csv_file, 'r') as infile, open(json_file, 'w') as outfile:
        reader = csv.DictReader(infile)
        transformed = []
        
        for row in reader:
            new_row = {
                "employeeId": row['emp_id'],
                "fullName": row['name'],
                "startDate": row['start_date'],
                "compensation": {
                    "baseSalary": float(row['salary']),
                    "currency": "USD"
                }
            }
            transformed.append(new_row)
        
        json.dump(transformed, outfile, indent=4)

if __name__ == '__main__':
    transform_csv_to_json('legacy_employees.csv', 'new_hris_format.json')
