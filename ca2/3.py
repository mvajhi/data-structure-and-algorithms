def main():
    inp = get_input()
    color_range = create_range(inp["list"])
    output = solve(color_range, inp["list"])
    print(output)

def solve(color_range, color_list):
    stack = list()
    open_num = 0
    level_count = 0
    for i in range(len(color_list)):
        if zero_not_ok(color_list[i], stack):
            return -1
        elif color_list[i] == 0:
            continue

        if is_this_color_just_repeat_once(color_range, color_list[i]):
            if open_num == level_count:
                level_count += 1
        elif is_end_of_range(color_range, color_list[i], i):
            open_num -= 1
            flag = remove_from_stack(stack, color_range[color_list[i]], color_list[i])
            if flag == False:
                return -1
        elif is_first_of_range(color_range, color_list[i], i):
            stack.append((color_list[i], i))
            if open_num == level_count:
                level_count += 1
            open_num += 1
        else:
            stack.append((color_list[i], i))

    return level_count

def remove_from_stack(stack, this_color_range, color):
    while(True):
        if len(stack) == 0:
            return True
        
        top = stack[len(stack) - 1]

        if top[1] == this_color_range[0]:
            stack.pop()
            return True
        if top[0] != color:
            return False
        
        stack.pop()

def is_end_of_range(color_range, color, index):
    return color_range[color][1] == index

def is_first_of_range(color_range, color, index):
    return color_range[color][0] == index

def is_this_color_just_repeat_once(color_range, color):
    return color_range[color][0] == color_range[color][1]

def zero_not_ok(color, stack):
    return color == 0 and len(stack) !=0

def cal_range_len(range):
    return range[1] - range[0] + 1

def create_range(color_string):
    color_range = dict()
    for i in range(len(color_string)):
        block_color = color_string[i]
        if block_color == 0:
            continue

        if block_color not in color_range.keys():
            color_range[block_color] = [i, i]
        else:
            color_range[block_color][1] = i
    # print("ranges: ", color_range)
    return color_range
            
def get_input():
    output = dict()
    output["count"] = int(input())
    output["list"] = list()
    for i in range(output["count"]):
        output["list"].append(int(input()))
    return output

if __name__ == "__main__":
    main()