# Write function bmi that calculates body mass index (bmi = weight / height2).
# if bmi <= 18.5 return "Underweight"
# if bmi <= 25.0 return "Normal"
# if bmi <= 30.0 return "Overweight"
# if bmi > 30 return "Obese"

def bmi(weight, height):
    #your code here
    result = weight / (height ** 2)
    result = round(result, 1)
    if result <= 18.5:
        return 'Underweight'
    elif result > 18.5 and result <= 25.0:
        return 'Normal'
    elif result > 25.0 and result <= 30.0:
        return 'Overweight'
    elif result > 30.0:
        return 'Obese'

case = bmi(82, 1.72)
print(case)