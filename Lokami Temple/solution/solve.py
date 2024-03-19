from collections import defaultdict

def find_longest_paths(num_doors, connections):
    graph = defaultdict(list)

    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)

    def dfs(node, visited):
        visited.add(node)
        max_path_length = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                path_length = dfs(neighbor, visited)
                max_path_length = max(max_path_length, path_length)
        visited.remove(node)
        return max_path_length + 1

    longest_paths = []

    for door in range(1, num_doors + 1):
        path_length = dfs(door, set())
        longest_paths.append((door, path_length))

    return longest_paths

def get_longest_paths(result):
    max_path_length = max(result, key=lambda x: x[1])[1]
    doors_with_max_length = [door for door, path_length in result if path_length == max_path_length]
    return max_path_length, doors_with_max_length

def main():
    num_doors = int(input(""))
    
    print("")
    connections = []
    for _ in range(num_doors - 1):
        a, b = map(int, input().split())
        connections.append((a, b))

    result = find_longest_paths(num_doors, connections)
    
    min_path_length = min(result, key=lambda x: x[1])[1]
    doors_with_min_length = [door for door, path_length in result if path_length == min_path_length]

    max_path_length, doors_with_max_length = get_longest_paths(result)

    print_exit = ' '.join(map(str, doors_with_max_length))
    print_door_min_length = ' '.join(map(str, doors_with_min_length))

    print(f"Entrance(s): {print_door_min_length}")
    print(f"Exit(s): {print_exit}")
    print(f"Path Length: {min_path_length - 1}")

if __name__ == "__main__":
    main()
