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
    def __init__(self, total_sum, balance_limit=None):
        self.total_sum = total_sum
        self.balance_limit = balance_limit
        self._balance = total_sum

    def __call__(self, sum_spent):
        if sum_spent > self.total_sum:
            raise ValueError(f'Not enough money to spend {sum_spent} dollars')
        self.total_sum -= sum_spent
        print(f'You spent {sum_spent} dollars.')

    def __str__(self):
        return 'To learn the balance call balance.'

    @property
    def balance(self):
        if self.balance_limit is not None:
            if self.balance_limit <= 0:
                raise ValueError('Balance check limits exceeded')
            self.balance_limit -= 1
        return self.total_sum

    def put(self, sum_put):
        self.total_sum += sum_put
        print(f'You put {sum_put} dollars.')

    def add(self, other):
        if isinstance(other, BankCard):
            new_total_sum = self.total_sum + other.total_sum
            new_balance_limit = max(self.balance_limit, other.balance_limit) if self.balance_limit and other.balance_limit else None
            return BankCard(new_total_sum, new_balance_limit)
