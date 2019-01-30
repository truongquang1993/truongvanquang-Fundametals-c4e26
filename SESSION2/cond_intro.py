yob = int(input("your birth of year?"))
age = 2019 - yob
print(age)

if age < 10: # age < 10: condition
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Adult")

print("Byebye")