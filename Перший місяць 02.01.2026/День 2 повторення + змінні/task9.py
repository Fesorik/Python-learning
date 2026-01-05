while True:
    name = input("Name or 'exit': ")
    if name.lower() == "exit":
        break
    age_input = input("Age: ")
    if not age_input.isdigit():
        print("Age must be a number")
    age = int(age_input)

    admin_permission = input("Are you admin? (yes/no): ").lower()
    is_admin = admin_permission == "yes"

    user = {
        "name" : name,
        "age" : age,
        "admin" : is_admin
    }
    if user["admin"] == "yes" or user["age"]>=18:
        print("Access granted")
    else:
        print("Access denied")