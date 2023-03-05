# task 1
# a = [1, 2, 3, 4, 5]
# x = '*'.join(str(i) for i in a)
# print(eval(x))

# task 2
# txt = input()
# cntup = 0
# cntlow = 0
# for i in txt:
#     if i.isupper():
#         cntup += 1
#     elif i.islower():
#         cntlow += 1
# print("Uppercase letters: ",cntup)
# print("Lowercase letters: ",cntlow)

# task 3
# txt = input()
# if txt == txt[::-1]:
#     print("String is palindrome")
# else:
#     print("String is not palindrome")

# task 4
# import time 
# num = int(input())
# milsec = int(input())
# sec = milsec/1000
# time.sleep(sec)
# sqrt = num ** 0.5
# txt = 'Square root of {fnum} after {fsec} is {fsqrt}'.format(fnum = num, fsec = milsec, fsqrt = sqrt)
# print(txt)

# task 5
# mytup = (True, True, False)
# mytup2 = (True, True, True)
# print(all(mytup))
# print(all(mytup2))
