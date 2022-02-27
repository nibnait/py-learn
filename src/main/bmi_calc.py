def calc(weight, height):
    bmi = (weight / height ** 2)
    return str(bmi)


weight = float(input("weight: "))
height = float(input("height: "))

bmi = calc(weight, height)
print("bmi: " + bmi)
