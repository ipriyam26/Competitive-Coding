# Modules Start
from __future__ import division, print_function
import sys
import os
# import time
from functools import reduce, cache, lru_cache # remove if CodeChef
from io import BytesIO, IOBase
import math
from collections import defaultdict
# Modules End

# Helpers
INT_MAX = 2147483647
INT_MIN = -2147483648
mod = int(1.e9) + 7
# Helpers End


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n,m = list(input().split(" "))
        number_of_digits_in_m = len(m)
        last_non_zero_digit = n.rstrip('0')
        if number_of_digits_in_m ==1:
            if last_non_zero_digit == '2':
                if m>'5':
                    print(int(n)*int(m))
                else:
                    print(int(n)*5)
            elif last_non_zero_digit == '5':
                if m != '1' and int(m) % 2 == 0 or m == '1':
                    print(int(n)*int(m))
                else:
                    print(int(n)*(int(m)-1))
            continue

        m_first_digit_place_value = m[0] + '0'*number_of_digits_in_m-1
        if last_non_zero_digit=='2':

            m_first_digit_place_value_temp = f'{m_first_digit_place_value[:1]}5{m_first_digit_place_value[2:]}'
            if m_first_digit_place_value_temp < m:
                m_first_digit_place_value = m_first_digit_place_value_temp
        elif last_non_zero_digit=='5':
            second_digit = int(m[1])
            if second_digit %2!=0:
                second_digit-=1
            m_first_digit_place_value = m_first_digit_place_value[:1]+second_digit+m_first_digit_place_value[2:]







        print(int(m_first_digit_place_value)*int(n))



# Settings
sys.setrecursionlimit(10000000)
# Settings End

# region fast_io
BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
# endregion


if __name__ == '__main__':
    main()
