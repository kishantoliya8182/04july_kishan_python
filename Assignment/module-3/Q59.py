# Q59. Write a Python program to convert degree to radian

def convert(degree):

    radian=degree * (3.14/180)

    print(f'Convertion after degree to radian: {radian}')

degree=int(input('Enter Degree: '))

convert(degree)