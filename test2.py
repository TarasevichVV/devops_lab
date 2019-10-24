s = input()
lengs = len(s)
lengs = lengs // 2
for i in range(lengs):
    if s[i] != s[-1 - i]:
        print("It's not palindrome")
        quit()
else:
    print("It's palindrome")
