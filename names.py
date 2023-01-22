print("Mam na imię Przemysław")  # tutaj wpisz swoje imię
# i dodaj jeszcze jakiś ciekawy kod

import random

numbers = []
dice = 12
times = 10
for i in range(times):
    number = random.randint(1, dice)
    numbers.append(number)

print(times, "rzutów kostką o", dice, "ściankach wynosi:", numbers)
