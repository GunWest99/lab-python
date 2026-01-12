# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)
#
#
#
# for i in range(3):
#     for j in range(3):
#         if i == j:
#             break
#         print(i,j)
#
#
#
# for i in range(1,4):
#     for j in range(3,6):
#         print(i, j)
#
#
#
# for i in range(1,4):
#     for j in range(3,5):
#         print(i, j, end='')
#
#
#
# counter=0
# for i in range(99,102):
#     temp=i
#     while temp>0:
#         counter +=1
#         temp //=10
# print(counter)
#
#
#
# a=int(input())
# for i in range(a):
#     print(a, a, a)
#
#
#
#
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,10):
#         b=i+j
#         print(i, '+', j, '=', b)
#     print()
#
#
#
# a=int(input())
# for i in range(1,a+1):
#     for j in range(a):
#         print()
#     print()
#
#
#
#
# a=int(input())
# for i in range(1, a+1):
#     for j in range(1,i+1):
#         print(i, end=' ')
#     print()
#
#
#
#
# a=int(input())
# for i in range(1, a+1):
#     for j in range(1,i+1):
#         print(j, end=' ')
#     print()
#
#
#
#
#
# total=0
# for x in range(1,65):
#     for y in range(1,60):
#         if 12*x+13*y==777:
#             total+=1
#             print('x=', x, 'y=', y)
# print('Общее количество натуральных решений=', total)
#
#
#
#
# b=int(input())
# a=int(input())
# for i in range(1, a+1):
#     for j in range(1, b+1):
#         print('*', end='')
#     print()
#
#
#
#
#
# a=int(input())
# for i in range(1, a+1):
#     for j in range(1, a+1):
#         print(j, end=' ')
#     print()
#
#
#
#
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1, i+1):
#         print('*', end='')
#     print()
#
#
#
#
# a=int(input())
# for i in  range(1,a+1):
#      print(a, '{i*j:4}', end='')



a=int(input())
b=int(input())
total=0
for x in range(1,a):
    for y in range(1,b):
        if 4*x+7*y==100:
            total+=1
            print('x=', x, 'y=', y)
print('Общее количество натуральных решений=', total)
