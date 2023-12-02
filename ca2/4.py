def main():
    inp = get_input()
    dict_of_way = create_dict(inp["way"])
    print("len num range: ", dict_of_way)
    solve(inp["shoes"], dict_of_way)

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
    print("before merge with smaller num: " ,dict_way)

    sorted_keys = sorted(dict_way.keys())
    print("sorted keys: ", sorted_keys)
    for i in range(len(sorted_keys) - 1):
        cur = dict_way[sorted_keys[i + 1]]
        pre = dict_way[sorted_keys[i]]
        # print()
        # print(tmp[i + 1])
        # print(pre)
        # print(cur)
        pre = change_range(pre, cur[0])
        # print(pre)
        pre = change_range(pre, cur[1])
        dict_way[sorted_keys[i + 1]] = pre
        # print(dict_way[tmp[i + 1]])
        # print()
        
    print("after merge with smaller num: ", dict_way)
    return {i: dict_way[i][1] - dict_way[i][0] for i in dict_way.keys()}

def solve(shoes, way):
    keys = way.keys()

    for i in shoes:
        key = convert_to_key(i[0], keys)
        if i[1] >= way[key]:
            print(1)
        else:
            print(0)

def convert_to_key(num, keys):
    if num in keys:
        return num

    return max(list(filter(lambda key: key < num, keys)))

if __name__ == "__main__":
    main()
