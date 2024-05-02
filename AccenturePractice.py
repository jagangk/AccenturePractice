num = int(input('enter the range: '))
n1 = 0
n2 = 1
if num <= 0:
    print('enter a valid number!')
elif num == 1:
    print(f'Fibonacci series: {num}')
else:
    print('fibonacci series:', n1, n2, end=" ")
    for i in range(2,num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")
