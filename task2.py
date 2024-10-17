import heapq

def merge_k_lists(lists):
    
    #додаємо всі елементи всіх масивів в одну купу
    merged_heap = []
    for list in lists:
        for number in list:
            heapq.heappush(merged_heap, number) 

    #витагуємо по одному елементу з купи в один спільний масив
    merged_list = []
    while len(merged_heap) > 0:
        merged_list.append(heapq.heappop(merged_heap))

    return merged_list

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)