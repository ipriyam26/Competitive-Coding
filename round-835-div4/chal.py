
test_cases = int(input())


for _ in range(test_cases):
    input()

    heights = [int(num) for num in input().split(" ")]

    end = len(heights)-1
    start = 1

    while start<end:
        if heights[start-1] < heights[start] and heights[start] > heights[start+1]:
            print("NO")
            break
        start+=1
    else:
        print("YES")