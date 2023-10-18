import copy
def main():
    num = input()
    is_find = is_misagi(num)
    print("YES" if is_find else "NO")


def is_misagi(num: str) -> bool:
    ans = dict()
    for i in range(1, len(num)):
        ans[0] = int(num[:i])
        for j in range(1, len(num)):
            ans[1] = int(num[i: i + j])

            if len(num[i + j:]) < len(str(ans[0] + ans[1])) or (num[i: i + j])[0] == "0":
                break

            # print(ans, num[i + j:])

            if is_ok(num[i + j:], ans):
                return True

    return False

def is_ok(num_input : str, two_first : dict) -> bool:
    ans = copy.deepcopy(two_first)
    num = copy.deepcopy(num_input)
    while len(num) > 0:
        len_ans = len(ans)
        next_num = str(ans[len_ans - 2] + ans[len_ans - 1])
        if next_num == num[:len(next_num)] and (num[:len(next_num)])[0] != "0":
            ans[len_ans] = int(next_num)
            num = num[len(next_num):]
        else:
            return False
    # print(ans)
    return True

if __name__ == "__main__":
    main()
