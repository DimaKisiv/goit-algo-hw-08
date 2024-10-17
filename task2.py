import heapq

def merge_k_lists_native(lists):
    return list(heapq.merge(*lists))

def merge_k_lists_heapify(lists):
    #обєднуємо всі масиви в один, перетворюємо його в купу, потім робимо з неї список
    merged_list_to_heap = []
    for list in lists:
        merged_list_to_heap.extend(list)
    #перетворюємо масив в купу
    heapq.heapify(merged_list_to_heap)
    return get_list_from_heap(merged_list_to_heap)
    
def merge_k_lists_heappush(lists):
    #додаємо всі елементи всіх масивів в одну купу, потім робимо з неї список
    merged_heap = []
    for list in lists:
        for number in list:
            heapq.heappush(merged_heap, number) 
    return get_list_from_heap(merged_heap)

def get_list_from_heap(heap):
    merged_list = []
    while heap:
        merged_list.append(heapq.heappop(heap))
    return merged_list

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list_native = merge_k_lists_native(lists)# з використанням вбудованої функції
merged_list_heapify = merge_k_lists_heapify(lists)# з використанням heapify для обєднаних масивів
merged_list_heappush = merge_k_lists_heappush(lists) # з використанням heappush для кожного елементу
print("Відсортований список:", merged_list_native)
print("Відсортований список:", merged_list_heapify)
print("Відсортований список:", merged_list_heappush)