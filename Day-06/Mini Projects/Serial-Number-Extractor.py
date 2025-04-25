serial_number = "INV-2024-APR-00098765"
first = serial_number.index("-")
year_test = serial_number[first+1:]
second = year_test.index("-")
month_test = year_test[second+1:]
third = month_test.index("-")
number_test = month_test[third+1:]


print(f"Year is {year_test[:second]}")
print(f"Month is {month_test[:third]}")
print(f"Serial Numer is {number_test[:]}\n\n\n")
#I DIDN'T KNOW THERE'S .split() function!

#Here's another code using .split after wasting my time thinking.

serial_number2 = "INV-2024-APR-00098765"

parts = serial_number2.split("-")

year2 = parts[1]
month2 = parts[2]
number_2 = parts[3]

print(f"Year is {year2}.")
print(f"Month is {month2}.")
print(f"Number is {number_2}.")