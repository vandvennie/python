user_input = input("Enter your age: ")  # taking input from user
print("hello, user. Your age is %s", user_input)

names = ["Tom", "Jerry", "Spike"]
age = [18,20,30]
for name, age in zip(names, age):
  print("user:", name, " age is ", age)