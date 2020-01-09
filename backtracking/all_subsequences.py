# pass

def generate_all_subsequences(sequence):
    create_state_space_tree(sequence, [], 0)


def create_state_space_tree(sequence, current_subsequence, index):
    if index == len(sequence):
        print(current_subsequence)
        return

    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.append(sequence[index])
    create_state_space_tree(sequence, current_subsequence, index + 1)
    current_subsequence.pop()

sequence = [3, 1, 2, 4]
generate_all_subsequences(sequence)

sequence = ["A", "B", "C"]
generate_all_subsequences(sequence)
