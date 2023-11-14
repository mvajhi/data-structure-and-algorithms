def main():
    inp = get_input()
    dict_of_way = create_dict(inp["way"])
    output = solve(inp, dict_of_way)
    print(output)

def get_input():
    output = dict()
    n, b = [int(i) for i in input().split(" ")]
    output["way"] = [int(i) for i in input().split(" ")]
    output["shoes"] = []
    for i in range(b):
        output["shoes"].append([int(i) for i in input().split(" ")])
    return output

def create_dict


if __name__ == "__main__":
    main()
