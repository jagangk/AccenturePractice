num = str(input('enter the number: '))
int_num = int(num)
sum = 0
while int_num > 0:
    digit = int_num % 10
    sum += digit ** len(num)
    int_num //= 10
if sum == int(num):
    print('armstrong number')
else:
    print('no')
