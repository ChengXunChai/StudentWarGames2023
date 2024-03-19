from collections import defaultdict

def calculate_memory_usage(p, q):
    children = defaultdict(list)
    memory = {}

    for a, b, c in p:
        memory[a] = c
        if b != 0:
            children[b].append(a)

    memo = {}
    results = []

    for query in q:
        stack = [query]
        total_memory = 0

        while stack:
            current_pid = stack.pop()
            if current_pid in memo:
                total_memory += memo[current_pid]
                continue

            total_memory += memory[current_pid]
            children_list = children[current_pid]

            for child in children_list:
                stack.append(child)

        results.append(total_memory)
        memo[query] = total_memory

    return results

N, Q = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(N)]
q = [int(input()) for _ in range(Q)]

results = calculate_memory_usage(p, q)
for result in results:
    print(result)
