inf = int(1e18)

for _ in range(int(input())):
    n, m, d = map(int, input().split())
    p = [int(x) for x in input().split()]
    array = [int(x) for x in input().split()]
    loc = {p[i]: i + 1 for i in range(n)}
    ans = inf
    cap = False

    for i in range(m - 1):
        left_a, right_b = inf, inf

        if loc[array[i]] < loc[array[i + 1]] <= loc[array[i]] + d:
            b_a = (loc[array[i + 1]] - loc[array[i]])
        else:
            cap = True
            break

        asdsa = (loc[array[i + 1]] - loc[array[i]])
        needed = (d - asdsa) + 1

        if loc[array[i]] - needed > 0:
            left_a = needed
        if loc[array[i + 1]] + needed <= n:
            right_b = needed

        left_over = (loc[array[i]] - 1) + (n - loc[array[i + 1]])
        req = inf
        if left_over - needed >= 0:
            req = needed

        ans = min(ans, b_a, right_b, left_a, req)

    if cap:
        print(0)
    else:
        print(ans)
