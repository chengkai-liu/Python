# pass

def generate_all_combinations(n, k):
    used_num = 0
    used_tag = [False for i in range(n + 1)]
    min_num = 1
    create_all_state(n, k, used_num, used_tag, min_num)
    
def create_all_state(n, k, used_num, used_tag, min_num):
    if used_num == k:
        result = []
        for i in range(1, n + 1):
            if used_tag[i] == True:
                result.append(i)
        print(*result)        
    
    for i in range(min_num, n + 1):
        if used_tag[i] == False:
            used_tag[i] = True
            if used_num == 0:
                min_num = i
            create_all_state(n, k, used_num + 1, used_tag, min_num)
            used_tag[i] = False


if __name__ == "__main__":
    ipt = input().strip()
    n, k = [int(ipt) for ipt in ipt.split(" ")]
    generate_all_combinations(n, k)
