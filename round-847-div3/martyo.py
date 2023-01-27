# Modules Start
from __future__ import division, print_function
import sys
import os
# import time
from io import BytesIO, IOBase
import math
from collections import defaultdict
from typing import List
# Modules End

# Helpers
INT_MAX = 2147483647
INT_MIN = -2147483648
mod = int(1.e9) + 7
# Helpers End
def search( nums: List[int], target: int) -> int:
    start = 0
    end = len(nums)-1
    while start<=end:
        mid = start + (end - start)//2
        if nums[mid]<target:
            start=mid+1
        elif nums[mid]>target:
            end= mid-1
        else:
            return mid
    return -1

def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        doll_sizes = [int(num) for num in input().split(" ")]
        doll_sizes.sort()
        current_top = []
        i=0

        while i<len(doll_sizes):
            if not current_top:
                current_top.append(doll_sizes[i])
                # total+=1
            else:
                current_doll_size = doll_sizes[i]
                rws = search(current_top,current_doll_size-1)
                print(rws,current_top,current_doll_size-1)
                if rws != -1: 
                    current_top[rws] = current_doll_size
                else:
                    current_top.append(current_doll_size)
            i+=1
        print(len(current_top))


# 2
# 1
# 6
# 2
# 2
# 2
# 2
# 2
# 4
# 3

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
