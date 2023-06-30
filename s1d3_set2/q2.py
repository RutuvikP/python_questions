numbers = [12, 75, 150, 180, 145, 525, 50]

for number in numbers:
    if number % 5 == 0 and number > 500:
        break
    elif number % 5 == 0 and number > 150:
        continue
    elif number % 5 == 0:
        print(number)