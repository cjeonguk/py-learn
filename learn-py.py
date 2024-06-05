age = 13

if age >= 18 and age <= 65:
    print('adult')

elif age <= 18 and age >= 13:
    print('teenager')

elif age < 13 and age >= 3:
    print('child')

elif not(age >= 3):
    print('baby')

elif age > 65 and age < 100:
    print('elderly')

elif age >= 100 or age < 0:
    print('centenarian or not born yet')