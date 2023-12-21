def main():
    inp = get_input()
    
    for q in inp["query"]:
        print(ans_query(inp, q))

def ans_query(inp, query):
    ans = 0
    for n in query:
        if inp["parent"][n] not in query:
            ans += inp["count_child"][n] + 1
        else:
            ans -= 1
    return ans
  
def get_input():
    out = dict()
    t, count = map(int, input().split())
    par = list(map(int, input().split()))
    out["parent"] = {i + 2: par[i] for i in range(t - 1)}
    # out["child"]  = {i + 1: [] for i in range(t)}
    out["count_child"] = {i + 1: 0 for i in range(t)}
    for i in range(t - 1):
        # out["child"][par[i]].append(i + 2)
        out["count_child"][par[i]] += 1
        
    out["query"] = list()
    for i in range(count):
        out["query"].append(list(map(int, input().split()))[1:])
    
    # print(out)
    return out

if __name__ == "__main__":
    main()