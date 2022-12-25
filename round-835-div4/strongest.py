# Modules Start
from __future__ import division, print_function
import sys
import os
# import time
from io import BytesIO, IOBase
import math

# Modules End

# Helpers
INT_MAX = 2147483647
INT_MIN = -2147483648
mod = int(1.e9) + 7
# Helpers End


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        leng = int(input())-1
        strengths = [int(participant) for participant in input().split(" ")]
        # if leng==0:
        #     print(0)
        #     continue
        strongest = max( strengths )
        second_strongest = max(strengths,key=lambda x: min(strengths)-1 if (x == strongest) else x)
        for i,strength in enumerate(strengths):
            if strength == strongest:
                print(strength-second_strongest,end="")
            else:
                print(strength-strongest,end="")
            if(leng!=i):
                print(" ",end="")
        print()
        # result = " ".join(
        #     str(strength - second_strongest)
        #     if strength == strongest
        #     else str(strength - strongest)
        #     for strength in strengths
        # )
        # print(result)
                




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
