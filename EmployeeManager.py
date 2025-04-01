def main():
    # Read employees from file
    try:
        with open('employees.txt', 'r') as file:
            employees = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        # Default list if file doesn't exist
        employees = [
            "John Smith",
            "Jackie Jackson",
            "Chris Jones",
            "Amanda Cullen",
            "Jeremy Goodwin"
        ]
        # Create the file with default data
        with open('employees.txt', 'w') as file:
            for employee in employees:
                file.write(employee + '\n')

    # Display current employees
    print(f"There are {len(employees)} employees:")
    for employee in employees:
        print(employee)

    # Prompt for employee to remove
    name_to_remove = input("\nEnter an employee name to remove: ")

    # Remove employee if found
    if name_to_remove in employees:
        employees.remove(name_to_remove)
        
        # Write updated list back to file
        with open('employees.txt', 'w') as file:
            for employee in employees:
                file.write(employee + '\n')
        
        # Display remaining employees
        print(f"\nThere are {len(employees)} employees:")
        for employee in employees:
            print(employee)
    else:
        print(f"\nError: Employee '{name_to_remove}' not found in the list.")

if __name__ == "__main__":
    main()
