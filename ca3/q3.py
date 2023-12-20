from heapq import heappop, heappush, heapify

def main():
    days, teachers = get_input()
    
    teachers.sort(key=lambda x: x["start"])
    heap = list()
    counter = 0
    
    for day in range(1, days + 1):
        while len(teachers) > counter and teachers[counter]["start"] <= day:
            heappush(heap, [-1 * teachers[counter]["angry"], teachers[counter]["day"]])
            counter += 1
        
        if len(heap) == 0:
            continue
        
        heap[0][1] -= 1
        if heap[0][1] <= 0:
            heappop(heap)
        
    output = 0
    for i,j in heap:
        output += -1 * i * j
    
    print(output)
        
def get_input():
    count, day = [int(i) for i in input().split(' ')]
    
    teachers = list()
    for _ in range(count):
        new_teacher = input().split(' ')
        teachers.append({
            "start" : int(new_teacher[0]),
            "day" : int(new_teacher[1]),
            "angry" : int(new_teacher[2]),
                         })

    return day, teachers

if __name__ == "__main__":
    main()