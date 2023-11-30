def main():
    inp = get_input()
    dict_of_way = create_dict(inp["way"])
    print(dict_of_way)
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

def change_range(old_range, num):
    new_range = old_range
    if old_range[0] < num and num < old_range[1]:
        if num - old_range[0] > old_range[1] - num:
            new_range = [old_range[0], num]
        else:
            new_range = [num, old_range[1]]

    return new_range

def create_dict(way):
    dict_way = dict()
    for i in range(len(way)):
        if not way[i] in dict_way.keys():
            dict_way[way[i]] = [0, len(way)]
        dict_way[way[i]] = change_range(dict_way[way[i]], i)

    tmp = sorted(dict_way.keys())
    for i in range(len(tmp) - 1):
        cur = dict_way[tmp[i + 1]]
        pre = dict_way[tmp[i]]
        # print()
        # print(tmp[i + 1])
        # print(pre)
        # print(cur)
        pre = change_range(pre, cur[0])
        # print(pre)
        dict_way[tmp[i + 1]] = change_range(pre, cur[1])
        # print(dict_way[tmp[i + 1]])
        # print()
        
    # print(dict_way)
    return {i: dict_way[i][1] - dict_way[i][0] for i in dict_way.keys()}


if __name__ == "__main__":
    main()
