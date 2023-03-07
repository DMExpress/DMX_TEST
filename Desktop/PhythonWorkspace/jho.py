p=int(input('가로의 길이 =>'))
q=int(input('세로의 길이 =>'))

m=min(p,q)

sum=0

for i in range (1, m + 1):
    num_square = (p - i + 1) * (q - i + 1)
    sum = sum + num_square

print('전체 정사각형 개수 :', sum)