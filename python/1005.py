from bisect import insort

class FoundOptimalSolution(Exception):
    pass

def solve(stones):
    minimum = float("inf")
    def find_min_difference(stones):
        nonlocal minimum
        if len(stones) == 1:
            minimum = min(stones[0], minimum)
            if minimum == 0 or minimum == 1:
                raise FoundOptimalSolution
            return
        largest = stones[-1]
        rest = sum(stones[:-1])
        if largest >= rest:
            minimum = min(largest - rest, minimum)
            if minimum == 0 or minimum == 1:
                raise FoundOptimalSolution
            return
        stones = list(stones)
        x = stones.pop()
        y = stones.pop()
        stones1 = list(stones)
        stones2 = list(stones)
        insort(stones1, abs(x - y))
        insort(stones2, x + y)
        find_min_difference(stones1)
        find_min_difference(stones2)
    try:
        find_min_difference(stones)
    except FoundOptimalSolution:
        pass
    print(minimum)

input() # ignore first line
stones = [int(word) for word in input().split()]
stones.sort()
solve(stones)
