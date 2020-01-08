# pass 3214,1234,123,-1234,123411,-128512,0
def make_heap(unsorted):
    heap = []
    while unsorted:
        heap.append(unsorted.pop())
        i = len(heap) - 1
        while i:
            if heap[(i - 1) // 2] > heap[i]:
                heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
                i = (i - 1) // 2
            else:
                break
    return heap

def heap_sort(unsorted):
    heap = make_heap(unsorted)
    while heap:
        unsorted.append(heap.pop(0))
    return unsorted

if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(heap_sort(unsorted))
