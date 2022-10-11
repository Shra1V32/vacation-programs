def check_if_last_digit_is_zero():
    num = int(input('Enter your number: '))
    num = str(num)
    if num[-1] == 0:
        print(f'The number has 0 at the end')
    else:
        print("The number doesn't have 0 at the end")

check_if_last_digit_is_zero()