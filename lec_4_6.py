#这是计算平均数的一个算法
n = eval(input('How many the number? : '))
sum = 0
for i in range(n):
    x = eval(input('Enter the number : '))
    sum = sum + x
sum = sum / n
print('\n The average is sum : ', sum)
