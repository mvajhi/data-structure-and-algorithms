def main():
    inp = get_input()
    dict_of_way_p = create_dict(inp["way"])
    #print("len num range: ", dict_of_way_p)
    dict_of_way_j = convert_p_to_j(dict_of_way_p,inp["way"])

    solve(inp["shoes"], dict_of_way_j, len(inp["way"]))

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

def better_than(r1, r2):
    return r1[1]-r1[0] < r2[1]-r2[0]

def create_dict(way):
    dict_way = dict()
    for i in range(len(way)):
        dict_way[way[i]] = [-1, len(way)]
    for i in range(len(way)):
        dict_way[way[i]] = change_range(dict_way[way[i]], i)
    #print("before merge with smaller num: " ,dict_way)

    sorted_keys = sorted(dict_way.keys())
    #print("sorted keys: ", sorted_keys)
    for i in range(len(sorted_keys) - 1):
        cur = dict_way[sorted_keys[i + 1]]
        pre = dict_way[sorted_keys[i]]
        # #print()
        # #print(tmp[i + 1])
        # #print(pre)
        # #print(cur)
        pre = change_range(pre, cur[0])
        # #print(pre)
        pre = change_range(pre, cur[1])
        if better_than(pre, cur):
            dict_way[sorted_keys[i + 1]] = pre
        # #print(dict_way[tmp[i + 1]])
        # #print()
        
    #print("after merge with smaller num: ", dict_way)
    return {i: dict_way[i][1] - dict_way[i][0] for i in dict_way.keys()}

def solve(shoes, way, len_way):
    for i in shoes:
        if i[1] <= 0:
            print(0)
            continue
        if i[1] >= len_way:
            print(1)
            continue
        if way[i[1]] <= i[0]:
            print(1)
        else:
            print(0)

def convert_p_to_j(p_dict : dict, way):
    sorted_key = sorted(p_dict.keys(), reverse=True)
    #print("sorted_key", sorted_key)
    j_p = {len(way) + 1: 0}
    for i in sorted_key:
        j_p[p_dict[i]] = i
    #print("j_p", j_p)
    sorted_key = sorted(j_p.keys())
    output = [0] * (len(way)+ 1)
    output[0] = -1
    for i in range(len(sorted_key)-1):
        for j in range(sorted_key[i], sorted_key[i + 1]):
            output[j] = j_p[sorted_key[i]]
    #print("output", output)
    return output

if __name__ == "__main__":
    main()
