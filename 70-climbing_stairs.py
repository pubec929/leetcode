def climbStairs(n: int):
    hashmap = {
        1: 1,
        2: 2
    }
    def _climbStairs(n: int):
        if n in hashmap:
            return hashmap[n]

        outcome = _climbStairs(n - 1) + _climbStairs(n - 2)
        hashmap[n] = outcome
        return outcome
    outcome = _climbStairs(n)
    return outcome

def climbStairs_v1(n: int):
    if n <= 2:
        return n
    
    a, b = 1, 2
    for _ in range(3, n):
        a, b = b, a + b
    return a + b


if __name__ == "__main__":
    print(climbStairs_v1(45))