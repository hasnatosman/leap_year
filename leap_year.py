print("I will check leap year in different way")
year = int(input("Input a number: "))
if year % 400 == 0:
    print("Yes")
elif year % 100 == 0:
    print("NO")
elif year % 4 == 0:
    print("Yes")
else:
    print("No")