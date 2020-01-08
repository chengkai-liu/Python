# pass 3214,1234,123,-1234,123411
def quick_sort(collection):
    length = len(collection)
    if length <= 1:
        return collection
    pivot = collection.pop()
    lesser, greater = [], []
    for element in collection:
        if element < pivot:
            lesser.append(element)
        else:
            greater.append(element)
    return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(quick_sort(unsorted))
