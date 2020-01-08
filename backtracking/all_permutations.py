# pass

def generate_all_permutations(sequence):
    create_state_space_tree(sequence, [], 0, [0 for i in range(len(sequence))])


def create_state_space_tree(sequence, current_sequence, index, index_used):
    if index == len(sequence):
        print(current_sequence)
        return

    for i in range(len(sequence)):
        if index_used[i] == False:
            current_sequence.append(sequence[i])
            index_used[i] = True
            create_state_space_tree(sequence, current_sequence, index + 1, index_used)
            current_sequence.pop()
            index_used[i] = False


sequence = [3, 1, 2, 4]
generate_all_permutations(sequence)

sequence = ["A", "B", "C"]
generate_all_permutations(sequence)
