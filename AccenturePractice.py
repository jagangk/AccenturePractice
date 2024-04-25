def findAutoCount(n):
    if n is None:
        return 0
    digit_count = [0] * 10

    for digit in n:
        digit_count[int(digit)] += 1

    for i,digit in enumerate(n):
        if digit_count[i] != int(digit):
            return False
    return True

n = str(input('Enter the number: '))
if findAutoCount(n):
    print(f'{n}autobiographical number')
    unique_digits = len(set(n))
    print(unique_digits)
else:
    print(f'{n}not an autobiographical number')
