def sumOrProduct(n, q):
    MOD = 10**9 + 7
    if q == 1:
        empty = 0
        for i in range(1,n+1):
            empty+=i
        return empty
    else:
        empty = 1
        for i in range(1,n+1):
            empty = (empty *i) % MOD
        return empty

print(sumOrProduct(15,2))