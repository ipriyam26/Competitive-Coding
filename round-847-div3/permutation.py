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
mod = int(1.0e9) + 7
# Helpers End


def main():
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        all_permutations = [[int(num) for num in input().split(" ")] for _ in range(n)]
        neighbours = {i: [[], []] for i in range(1, n + 1)}
        for permutations in all_permutations:
            for i, element in enumerate(permutations):
                if i == 0:
                    neighbours[element][0].append("S")
                    neighbours[element][1].append(permutations[i + 1])

                elif i == len(permutations) - 1:
                    neighbours[element][0].append(permutations[i - 1])
                    neighbours[element][1].append("L")
                else:
                    neighbours[element][0].append(permutations[i - 1])
                    neighbours[element][1].append(permutations[i + 1])
        # guessing neighbours now
        results = {}
        for key,value in neighbours.items():
            left = max(set(value[0]), key=value[0].count)
            right = max(set(value[1]), key=value[1].count)
            results[key] = (right,left)
        
        stack = [1]
        visited = [-1]*(n+1)
        solution=[1]
        if n<=4:
            continue
        while stack: 
            element = stack.pop()
            if visited[element]!=-1:
                continue
            visited[element] = 0
            children = results[element]
            right,left = children
            element_location = solution.index(element)
            if left=='S' or visited[left] ==-1:
                solution.insert(element_location-1,left)
            if right == 'L' or visited[right] ==-1:
                solution.insert(element_location+1,right)
            for child in children:
                stack.insert(0,child)
        print(solution)
        print()



# {
#     1: [[2, 2, 4], ["L", 3, 3]],
#     2: [[4, 4, "S"], [1, 3, 1]],
#     3: [[2, 1, 1], ["L", "L", "L"]],
#     4: [["S", "S", "S"], [2, 2, 1]],
# }
# {
#     1: [["S", "S"], [3, 2]],
#     2: [["S", 1], [3, "L"]],
#     3: [[2, 1], ["L", "L"]],
# }
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


if __name__ == "__main__":
    main()
