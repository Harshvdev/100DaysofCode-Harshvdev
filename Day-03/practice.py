#Day-3

monthconversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthconversions["Mar"])

#while loop

i = 1

while i <= 10:
    print(i)
    i = i+1

print(range(i))



for i in range(9, 19):
     print(i)


def expo(base, pow): #Enter base number and power
    result = 1
    for i in range(pow): #Loops pow times
        result = base*result #multiplies base*result pow times. Basically multiplies the base num pow times.
    return result

print(expo(2, 3)) #8