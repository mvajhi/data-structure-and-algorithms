def main():
    N, list_of_num = get_input()
    for i in range(N + 1):
        print(play(i, list_of_num, N))
    pass

def get_input():
    N = int(input())
    list_str = input()
    num_list = [int(i) for i in list_str if i != " "]
    return N, num_list

def play(num, list_of_num, N):
    pre = 0
    result = 0
    rmin = 0
    rmax = N + 1
    for guess in list_of_num:
        if rmin <= num and num <= rmax:
            ans = 1 if num < guess else 0

            if ans == 0 and pre == 1:
                result += 1
            pre = ans

            # posable bug
            if ans == 1:
                rmax = guess
            else:
                rmin = guess
            if rmax - rmin == 1:
                break
    return result

if __name__ == "__main__":
    main()