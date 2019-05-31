# taxes.py
income = 103000
if income < 10000:
    tax_coefficient = 0.0
elif income < 30000:
    tax_coefficient = 0.2
elif income < 1000000:
    tax_coefficient = 0.35
else:
    tax_coefficient = 0.45

print(f"I will pay {income * tax_coefficient} in taxes")
