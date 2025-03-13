a=int(input("Enter count: "))
max = 0
for i in range a:
  n = int(input("Enter a number: "))
  if n > max and n < 30000 and n%3 == 0 and n%2 == 1:
    max =n

print(n)
