user = {
    "name" : input("Your name: "),
    "sex" : input("Your sex: "),
    "age" : int(input("Your age: "))
}
if user["age"]>=18:
    print("Is adult")
else:
    print("Not adult")
print(user)