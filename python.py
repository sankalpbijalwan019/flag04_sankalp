employee_table = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

def search_employee_data(search_parameter):
    if search_parameter == 1:
        age = int(input("Enter age: "))
        for employee in employee_table:
            if employee["Age"] == age:
                print(employee)
    elif search_parameter == 2:
        name = input("Enter name: ")
        for employee in employee_table:
            if employee["Name"] == name:
                print(employee)
    elif search_parameter == 3:
        salary_operator = input("Enter salary operator (<, >, <= or >=): ")
        salary = int(input("Enter salary: "))
        for employee in employee_table:
            if salary_operator == "<" and employee["Salary (PM)"] < salary:
                print(employee)
            elif salary_operator == ">" and employee["Salary (PM)"] > salary:
                print(employee)
            elif salary_operator == "<=" and employee["Salary (PM)"] <= salary:
                print(employee)
            elif salary_operator == ">=" and employee["Salary (PM)"] >= salary:
                print(employee)

search_parameter = int(input("Enter search parameter (1 for Age, 2 for Name, and 3 for Salary): "))
search_employee_data(search_parameter)