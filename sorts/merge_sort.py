# pass 3214,1234,123,-1234,123411
def merge_sort(collection):
    def merge(left, right):
        result = []
        while left and right:
            if (left[0] <= right[0]):
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        return result + left + right

    if len(collection) <= 1:
        return collection
    mid = len(collection) // 2
    return merge(merge_sort(collection[:mid]), merge_sort(collection[mid:]))


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    unsorted = [int(item) for item in user_input.split(",")]
    print(*merge_sort(unsorted), sep=",")
