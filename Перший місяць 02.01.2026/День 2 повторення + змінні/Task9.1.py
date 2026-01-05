while True:
        def create_user():
            name = input("Name or 'exit': ")
            if name.lower() == "exit":
                return None
            age_input = input("Age: ")
            if not age_input.isdigit():
                print("Age must be a number")
                return None
        
            age = int(age_input)

            admin_permission = input("Are you admin? (yes/no): ").lower()
            is_admin = admin_permission == "yes"

            return {
            "name": name,
            "age": age,
            "is_admin": is_admin
        }
        
        def check_access(user):
            if user["admin"] == "yes" or user["age"]>=18:
                return True
            return False