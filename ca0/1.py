def main():
    input_str = input()
    count = calculate(input_str)
    print(count)

def calculate(txt: str) -> int:
    counter = 0
    len_txt = len(txt)

    for i in range(len_txt):
        counter_per_char = {i : 0 for i in ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]}
        for j in range(i + 1, len_txt + 1):
            counter_per_char[txt[j - 1]] += 1
            if is_ok(counter_per_char):
                counter += 1
    
    return counter
            
def is_ok(counter_per_char : dict) -> bool:
    odd_counter = 0
    
    for i in counter_per_char.values():
        if i % 2 == 1:
            odd_counter += 1
    
    if odd_counter <= 1:
        return True
    else:
        return False
            

if __name__ == "__main__":
    main()
