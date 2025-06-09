import csv

def export_legacy_data():
    employees = [
        {'emp_id': '001', 'name': 'Jane DevOps', 'start_date': '2022-04-01', 'salary': '98000'},
        {'emp_id': '002', 'name': 'John Infra', 'start_date': '2021-08-15', 'salary': '89000'},
    ]
    
    with open('legacy_employees.csv', 'w', newline='') as csvfile:
        fieldnames = ['emp_id', 'name', 'start_date', 'salary']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)

if __name__ == '__main__':
    export_legacy_data()
