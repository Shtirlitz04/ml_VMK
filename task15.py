from typing import List


def hello(x=None):
    if x==None or x == '':
        return 'Hello!'
    else:
        return 'Hello, ' + x + '!'
        

def int_to_roman(num):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["", "X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["", "I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
    thousands = m[num // 1000]
    hundreds = c[(num % 1000) // 100]
    tens = x[(num % 100) // 10]
    ones = i[num % 10]
 
    ch = (thousands + hundreds +
           tens + ones)
    ans = str(ch).replace(" ","")
    return ans
    


def longest_common_prefix(arr):
    min_str = ''
    if arr:
        min_str = min(s.lstrip() for s in arr)
        for i in range(len(min_str)):
            for s in arr:
                s = s.lstrip()
                if s[i] != min_str[i]:
                    return min_str[:i]
    return min_str


def primes():
    yield 2
    n = 3
    while True:
        ind = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                ind = False
                break
        if ind:
            yield n
        else:
            ind = True
        n += 2


class BankCard:
    pass
