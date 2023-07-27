#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fn(n):
 if n == 1:
    return 0
 elif n == 2:
    return 1
 else:
    return fn(n-1) + fn(n-2)

num = int(input("Enter a number : "))
if num > 0:
 print("fn(", num, ") = ",fn(num) , sep ="")
else:
 print("Error in input")


# In[2]:


def bin2Dec(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
        i += 1
    return dec

def oct2Hex(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8**i
        i += 1
    result_list = []
    while dec != 0:
        result_list.append(dec % 16)
        dec = dec // 16

    hex_list = []
    for elem in result_list[::-1]:
        if elem <= 9:
            hex_list.append(str(elem))
        else:
            hex_list.append(chr(ord('A') + (elem - 10)))

    hex_val = "".join(hex_list)
    return hex_val

num1 = input("Enter a binary number: ")
print(bin2Dec(num1))

num2 = input("Enter an octal number: ")
print(oct2Hex(num2))


# In[ ]:




