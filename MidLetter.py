# Middle letter
# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

# For example, mid("abc") should return "b" and mid("aaaa") should return "".

# Method 1:

def mid(string):
    if len(string) % 2 == 0:
        return ""
    print(string[len(string)//2])
    return string[len(string)//2]
    
# Method 2:(Using math.ceil)
def mid(strParam):
     n= len(strParam)
     if n%2==0:
     	middle =""
     else:
     	middleindex = (math.ceil(n/2))-1
     	middle=strParam[middleindex]
     print(middle)
     return middle

mid("abc")