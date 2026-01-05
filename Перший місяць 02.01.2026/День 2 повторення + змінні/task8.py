user = {
    "name" : input("Your name: "),
    "age" : int(input("Your age: ")),
    "permission" : input("Do you admin? ")
}
age = user.get("age")
permission = user.get("permission")
is_admin = permission == "yes"

if is_admin or age>=18:
    print("Access granted")
else:
    print("Access denied")
