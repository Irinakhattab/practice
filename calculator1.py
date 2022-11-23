print('введите число a=')
a = int(input())

print('введите число b=')
b = int(input())

print('выберите операцию')
print('1 - сложить a + b')
print('2 - вычесть a - b')
print('3 - умножить a * b')
print('4 - разделить a / b')

d = int(input())

if d==1:
    print('сумма a+b=' , a+b)

if d==2:
    print('разность a-b=' , a-b)

if d==3:
    print('умножение a*b=' , a*b)

if d==4:
    print('деление a/b=' , a/b)
