n, m = map(int, input().split())
Array = input().split()
A = set(input().split())
B = set(input().split())
happy = 0
for i in Array:
    if i in A:
        happy += 1
    if i in B:
        happy -= 1
print(happy)
