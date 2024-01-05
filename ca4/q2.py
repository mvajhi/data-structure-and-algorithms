from itertools import permutations

def main():
    n, t, queries = get_input()
    ans = pre_process(n)
    print_output(ans, queries)

def pre_process(n):
    count = create_dict(n)
    sort_l = tuple(i for i in range(n))
    count[sort_l] = 0
    queue = [sort_l]
    
    bfs(queue, n, count)
    
    return count

def bfs(queue, n, count):
    while len(queue) != 0:
        state = queue.pop(0)
        for i in range(n + 1):
            for j in range(i + 2, n + 1):
                new_state = create_new_state(state, i, j)
                
                if count[new_state] == -1:
                    count[new_state] = count[state] + 1
                    queue.append(new_state)

def create_new_state(state, i, j):
    new_state = list(state)
    new_state[i:j] = reversed(new_state[i:j])
    new_state = tuple(new_state)
    return new_state  
    
def create_dict(n):
    l = [i for i in range(n)]
    return {i:-1 for i in permutations(l)}

def print_output(ans, queries):
    for q in queries:
        print(ans[q])
        
def get_input():
    n = int(input())
    t = int(input())
    
    queries = list()
    for _ in range(t):
        first, end = input().split()
        query = convert_to_query(n, first, end)
        queries.append(query)
    
    return n, t, queries

def convert_to_query(n, first, end):
    binding = dict()
    for i in range(n):
        binding[end[i]] = i
    
    return tuple(binding[i] for i in first)

if __name__ == "__main__":
    main()