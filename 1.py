n = int(input("Enter count: "))
max = 0
for i in range n:
    a = int(input("Enter number: "))
    if a % 3 == 0 and a < 30000 and a > 0 and a%2 == 0:
      max = a

print(max)
