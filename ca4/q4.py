def main():
    inp = get_input()
    print(inp)
    out = solve()
    print(out)

def get_input():
    n, m, k = map(int, input().split())
    edge = list()
    for _ in range(k):
        edge.append(list(map(int, input().split())))
    
    return {
        'n':n,
        'm':m,
        'k':k,
        'e':edge
    }


if __name__ == "__main__":
    main()