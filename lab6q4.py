def calculate_bmi(weight, height):
    """Calculate and return the Body Mass Index (BMI)."""
    return weight / (height ** 2)

# FUNCTION CALL usage
print(round(calculate_bmi(70, 1.75), 2))  # Approx. 22.86