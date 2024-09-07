name = input ("Insert your name: ")
monthly_salary = float (input ("Insert your monthly salary in dollars: "))
annual_salary = monthly_salary * 12
annual_salary_in_thousands = annual_salary / 1000
print (f"{name}, your annual salary is: {annual_salary_in_thousands: .0f} thousand dollars.")

number = int (input ("Insert a number: "))
is_even = (number % 2 == 0)
is_in_range = (100 <= number <= 999)
if is_even and is_in_range: print (True)
else: print (False)

number = int (input("Insert a number in range 101 - 999: "))
number_str = str (number)
reversed_number_str = number_str[::-1]
reversed_number = int (reversed_number_str)
print (reversed_number)

num1 = int (input ("Insert first number: "))
num2 = int (input ("Insert second number: "))
sum_result = num1 + num2
diff = num1 - num2
prod = num1 * num2
if num2 != 0:
  div = num1 / num2
  remain = num1 % num2
else:
  div = "Division on zero is not possible"
  remain = "Division on zero is not possible"
comparison = num1 >= num2

print (f"Summa: {sum_result}")
print (f"Difference: {diff}")
print (f"Produkt: {prod}")
print (f"Division: {div}")
print (f"Remainder: {remain}")
print (f"Is num1 >= num2: {comparison}")
