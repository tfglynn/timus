K = int(input())
groups = [int(word) for word in input().split()]
groups.sort()
print(sum([group // 2 + 1 for group in groups[:K // 2 + 1]]))
