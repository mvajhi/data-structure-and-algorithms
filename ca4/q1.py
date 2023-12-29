def main():
    inp = get_input()
    print(inp)
    out = solve(inp)
    print(out)
    
def get_input():
    output = dict()
    output["V_count"], output["E_count"] = map(int, input().split())

    output["E"] = list()
    for _ in range(output["E_count"]):
        new_e = list(map(int, input().split()))
        output["E"].append(new_e)
        
    return output
    
    
if __name__ == "__main__":
    main()