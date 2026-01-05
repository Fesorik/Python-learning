user = {
    "name" : input("Your name: "),
    "sex" : input("Your sex: "),
    "age" : int(input("Your age: "))
}
age = user["age"] # another age = user.get("age")
is_adult = age>=18

if is_adult:
    print("Adult")
else:
    print("Not Adult")
print(user)

# Normal code
# if age is None:
#     print("Age not specified")
# elif age>=18:
#     print("Adult")
# else:
#     print("Not Adult")
# print(user)