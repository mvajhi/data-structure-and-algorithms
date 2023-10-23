def create_new_bitmap(bit_map, char):
    bit_place = ord(char) - ord("a")
    
    bit_map[bit_place] = (bit_map[bit_place] + 1) % 2
    
    return bit_map


txt = input()

result = 0
odd_bitmap_list = [0 for i in range(10)]
my_str = ""
ans = dict()

for char in txt:
    my_str += char
    odd_bitmap_list = create_new_bitmap(odd_bitmap_list, char)
    odd_bitmap = tuple(odd_bitmap_list)
    

    if odd_bitmap.count(1) <= 1:
        result += 1
    
    if odd_bitmap in ans.keys():
        result += ans[odd_bitmap]
        ans[odd_bitmap] += 1
    else:
        ans[odd_bitmap] = 1

    for i in range(len(odd_bitmap)):
        tmp = list(odd_bitmap)
        tmp[i] = (tmp[i] + 1) % 2
        tmp = tuple(tmp)
        
        if tmp in ans.keys():
            result += ans[tmp]

print(result)