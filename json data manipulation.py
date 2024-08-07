import json

salary_threshold = 10000
with open('employees.json', 'r') as file:
    employees = json.load(file)
filtered_employees = [employee for employee in employees if employee.get('salary', 0) > salary_threshold]
for employee in filtered_employees:
    print(f"ID: {employee['id']}, Name: {employee['first_name']} {employee['last_name']}, "
          f"Job Title: {employee['job_title']}, Salary: ${employee['salary']}")
with open('filtered_employees.json', 'w') as outfile:
    json.dump(filtered_employees, outfile, indent=4)

print("Filtered data has been written to 'filtered_employees.json'")