def main():
    inp = get_input()
    list_final = create_dict(inp["way"])
    ok_list = convert_to_ok_list(list_final,inp["way"])
    #print("len num range: ", dict_of_way_p)
    #print(inp["shoes"])

    output = solve(inp["shoes"], ok_list, len(inp["way"]))
    print_output(output)

def convert_to_ok_list(l, way):
    way = sorted(way)
    out = list()
    for i in range(len(l)):
        out.append([way[i], l[i]])
    # print("ok_out",out)
    return out

def print_output(out):
    for i in out:
        print(i)

def get_input():
    output = dict()
    n, b = [int(i) for i in input().split(" ")]
    output["way"] = [int(i) for i in input().split(" ")]
    output["shoes"] = []
    for i in range(b):
        output["shoes"].append([*[int(i) for i in input().split(" ")], i])
    return output

def create_dict(way):
    l1 = convert_to_min_index_list(way, -1)
    # print("l1: ",l1)
    l2 = convert_to_min_index_list(list(reversed(way)), -1)
    for i in range(len(l2)):
        if l2[i] == -1:
            l2[i] = len(way)
        else:
            l2[i] = len(way) - 1 - l2[i]
    # print("l2: ",list(reversed(l2)))
    lf = convert_l1_l2_to_lf(l1, l2, way)
    # print("lf: ",lf)
    my_list = [[way[i], i] for i in range(len(way))]
    my_list = sorted(my_list, key=lambda t: t[0]) 
    # print("my",my_list)
    
    m = -2
    out = list()
    for i in range(len(my_list) - 1, -1, -1):
        m = max(m, lf[my_list[i][1]])
        out.append(m)
    out = list(reversed(out))
    # print("out ", out)
    return out

def convert_l1_l2_to_lf(l1, l2, way):
    # new_l1, new_l2 = create_new_l1_l2(l1, l2, way)
    #print(new_l1, new_l2)
    lf = list()
    for i in range(len(l1)):
        lf.append( l2[len(l1) - 1 - i] - l1[i] - 1)
    #print("lf", lf)
    return lf


def create_new_l1_l2(l1, l2, way):
    new_l1 = dict()
    for i in l1:
        new_l1[i[0]] = len(way) + 1
    
    new_l2 = dict()
    for i in l2:
        new_l2[i[0]] = -2

    for i in l1:
        if i[1] < new_l1[i[0]]:
            new_l1[i[0]] = i[1]

    for i in l2:
        if i[1] > new_l2[i[0]]:
            new_l2[i[0]] = i[1]
    return new_l1, new_l2

def convert_to_min_index_list(inp_list, end_num):
    output = list()
    stack = list()
    for i in range(len(inp_list)):
        while(True):
            if len(stack) == 0:
                output.append(end_num)
                if i < len(inp_list)-1 and inp_list[i] < inp_list[i+1]:
                    stack.append([inp_list[i], i])
                break
            if stack[-1][0] < inp_list[i]: 
                output.append(stack[-1][1])
                if i < len(inp_list)-1 and inp_list[i] < inp_list[i+1]:
                    stack.append([inp_list[i], i])
                break
            else:
                stack.pop()

    return output

def solve(shoes, list_final, len_way):
    list_final = sorted(list_final, key=lambda t: t[0]) 
    # print(list_final)
    new_dict = dict()
    for i in list_final:
        new_dict[i[0]] = i[1]
    for i in list_final:
        new_dict[i[0]] = max(i[1], new_dict[i[0]])
    # list_final= new_dict
    # print(new_dict)
    sorted_key = sorted(new_dict.keys())
    #print(sorted_key)
    sorted_shoes = sorted(shoes, key=lambda t: t[0]) 
    # print(sorted_shoes)
    #print("sorted_key ",sorted_key)
    index_list = 0
    output = [0] * len(shoes)

    # print(list_final)
    # print(shoes)

    index = 0
    for i in range(len(sorted_shoes)):
        while (True):
            if index >= len(list_final):
                break
            if list_final[index][0] > sorted_shoes[i][0]:
                break
            index += 1
        if index == 0:
            if sorted_shoes[i][1] > len_way:
                output[sorted_shoes[i][2]] = 1
        else:
            if index == len(list_final) or sorted_shoes[i][1] > list_final[index][1]:
              if sorted_shoes[i][1] > 0:
                output[sorted_shoes[i][2]] = 1
    
    
    return output

if __name__ == "__main__":
    main()
