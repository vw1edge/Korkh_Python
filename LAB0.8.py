import random

secret_code = random.randint(1, 100)
while True:
    guess = int(input("введите пинкод"))
    if guess < secret_code:
        print("Вывод: Больше")
    elif guess > secret_code:
        print("Вывод: Меньше")
    else:
        print("Вывод: Код подобран!")
        break