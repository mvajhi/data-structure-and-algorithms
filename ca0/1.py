def main():
    input_str = input()
    count = calculate(input_str)
    print(count)

def calculate(txt: str) -> int:
    counter = 0
    len_txt = len(txt)

    for i in range(len_txt):
        list_of_odd_word = []
        for j in range(i + 1, len_txt + 1):
            if txt[j-1] in list_of_odd_word:
                list_of_odd_word.remove(txt[j-1])
            else:
                list_of_odd_word.append(txt[j-1])

            if len(list_of_odd_word) <= 1:
                counter += 1
    
    return counter 

if __name__ == "__main__":
    main()
