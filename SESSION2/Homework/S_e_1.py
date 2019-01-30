height = int(input("Input your height (cm): "))
weight = int(input("Input your weight (kg): "))

n = 0.01*height
BMI = weight/(n*n)

if  BMI < 16:
    print("severely underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("Normal")
elif BMI < 30:
    print("overweight")
else:
    print("obese")