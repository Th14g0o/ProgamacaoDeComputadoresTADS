n1 = int(input())
n2 = int(input())
n = n2 - n1
hora = n // 60
min = n % 60

print("{:02d}:{:02d}".format(hora, min))