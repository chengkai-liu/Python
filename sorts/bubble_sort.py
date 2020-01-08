# pass
def bubble_sort(collection):
    length = len(collection)
    for i in range (length - 1):
        swapped = False
        for j in range(length - i - 1):
            if (collection[j] > collection[j + 1]):
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
                swapped = True
        if not swapped:
            break
    return collection


if __name__ == "__main__":
    import time

    user_input = input("Enter numbers separated by a comma:").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    start = time.process_time()
    print(*bubble_sort(unsorted), sep=",")
    print(f"Processing time: {time.process_time() - start}")
