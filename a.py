for number in range(1, 41):
    if number % 3 == 0 or "3" in str(number):
        print("スパルタ！")
    else:
        print(number)
