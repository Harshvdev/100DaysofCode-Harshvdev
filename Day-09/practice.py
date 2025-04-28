s = "        Fly me to the moon                "
print(len(s.split()[-1]))

num = [3, 3]
target = 6
for a in num:
    for b in num:
        print(num.index(a), num.index(b))
        if a+b == target:
            print(num.index(a), num.index(b))
        else:
            print("Null")
print("")
#Can't understand it.
for i in num:
    print(num.index(i))
#Hmmm, I understood the problem is with .index(). It gives the index of the FIRST occurence if the number.
#That's why if there are multiple same numbers, it returns the very first value's index.
print("")
for index in range(len(num)):
    print(index)
#I just learned about enumerate(), I'll use that.
for indexa, valuea in enumerate(num):
    for indexb, valueb in enumerate(num):
        if valuea+valueb == target and indexa < indexb:
            print(indexa, indexb)
        else:
            pass