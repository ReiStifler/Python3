n1, n2, n3 = input().split()
# n2 = float(input())
# n3 = float(input())
p1, p2, p3 = input().split()
# p2 = int(input())
# p3 = int(input())

ponderada = ((float(n1)*int(p1))+(float(n2)*int(p2)) +
             (float(n3)*int(p3)))/((int(p1)+int(p2)+int(p3)))
print("%6f" % ponderada)
# n1*p1 + n2*p2 + n3*p3
# ((float(n1*p1 + n2*p2 + n3*p3)) / (int(p1+p2+p3)))
