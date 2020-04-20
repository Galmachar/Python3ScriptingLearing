#!/usr/bin/env python

#BMI = (waga w kg / wysokość w metrach^2)
def gather_info():
    height = float(input("What is your height in meters?: "))
    weight = float(input("What is your weight in kilograms??: "))
    return weight, height

def calculate_bmi(weight,height):
    #returns Body Mass Index (BMI)
    return (weight/(height**2))
def r_u_fat(bmi):
    if bmi < 18.5:
        return "u skinny"
    elif bmi > 25:
        return "u fat"
    else:
        return "u normal"
def main():
    #unpacking tuple
    weight, height = gather_info()
    #values=gather_info()
    #bmi = round(calculate_bmi(values[0],values[1]) * 10000, 2)
    bmi = round(calculate_bmi(weight,height) * 10000, 2)
    print(f"your bmi is {bmi} and " + r_u_fat(bmi))
main()