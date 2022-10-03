def isPalindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False

if '__main__' == __name__:
    print(isPalindrome(int(input())))