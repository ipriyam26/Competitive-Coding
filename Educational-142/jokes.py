# Modules Start
from __future__ import division, print_function
import sys
import os
# import time
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

        a1b1,a1b0,a0b1,a0b0 = [int(num) for num in input().split(" ")]
        A,B = a1b1,a1b1
        total_jokes = a1b1

        while   A>=0 and B>=0:

            # lets try to reduce A to zero
            jokes_needed_for_a_to_0 = min(a0b1,A)
            if jokes_needed_for_a_to_0==0:
                break
            # we can tell ^ many a1b0 jokes
            total_jokes+=jokes_needed_for_a_to_0
            a0b1-=jokes_needed_for_a_to_0

            #update A and B
            A,B = A-jokes_needed_for_a_to_0,B+jokes_needed_for_a_to_0

            # now we take B to zero
            jokes_needed_for_b_to_0 = min(a1b0,B)
            if jokes_needed_for_b_to_0 ==0:
                break
            # we can tell ^ of a1b0 jokes
            total_jokes+=jokes_needed_for_b_to_0
            a1b0-=jokes_needed_for_b_to_0

            #update A and B
            A,B = A+jokes_needed_for_b_to_0,B-jokes_needed_for_b_to_0
        can_break = min(A,B)+1

        if a0b0<=can_break:
            can_break-=a0b0
            total_jokes+=a0b0
            A,B = A-a0b0,B-a0b0
            total_jokes += min(A+1,a0b1) if a1b0==0 else min(B+1,a1b0)
        else:
            total_jokes += can_break
        print(total_jokes)



        



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
