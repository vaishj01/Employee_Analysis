import csv
from functools import reduce
import matplotlib.pyplot as plt

# Load CSV file and return a list of dictionaries
def load_csv(file_path):
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

# Display all employees
def display_employees(data):
    print("\n--- All Employees ---")
    for emp in data:
        print(emp)

# Filter employees by designation
def filter_by_designation(data, designation='manager'):
    return list(filter(lambda e: e['Designation'].lower() == designation.lower(), data))

# Sort employees by salary
def sort_by_salary(data, descending=False):
    return sorted(data, key=lambda e: int(e['Salary']), reverse=descending)

# Calculate total and average salary
def total_and_average_salary(data):
    total = reduce(lambda acc, e: acc + int(e['Salary']), data, 0)
    average = total / len(data) if data else 0
    return total, average

# Plot bar chart of salaries
def plot_salary_distribution(data):
    names = [e['Name'] for e in data]
    salaries = [int(e['Salary']) for e in data]
    plt.bar(names, salaries, color='Brown')
    plt.xlabel('Employee Name')
    plt.ylabel('Salary')
    plt.title('Employee Salary Distribution')
    plt.tight_layout()
    plt.show()

# Menu-driven CLI
def run_menu(file_path):
    employees = load_csv(file_path)
    while True:
        print("\n==== EMPLOYEE DATA ANALYSIS MENU ====")
        print("1. Show all Employees")
        print("2. Filter by Designation")
        print("3. Sort by Salary (Low to High)")
        print("4. Total and Average Salary")
        print("5. Show Graph: Salary Distribution")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            display_employees(employees)
        elif choice == '2':
            designation = input("Enter designation to filter (e.g., HR, manager): ")
            filtered = filter_by_designation(employees, designation)
            display_employees(filtered)
        elif choice == '3':
            sorted_employees = sort_by_salary(employees)
            display_employees(sorted_employees)
        elif choice == '4':
            total, average = total_and_average_salary(employees)
            print(f"\nTotal Salary: ₹{total}, Average Salary: ₹{average:.2f}")
        elif choice == '5':
            plot_salary_distribution(employees)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

# Run the menu with your CSV file path
run_menu("D:/Gryphon Python/Day-4/emp.csv")
