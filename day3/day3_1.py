def get_max(arr):
    arr = [int(x) for x in arr]
    maxim = max(arr)
    position = arr.index(maxim)
    
    return str(maxim), position


banks = open('input.txt', 'r').readlines()
banks = [rotation.replace('\n', '') for rotation in banks]

total = 0
for bank in banks:
    first_max, first_pos = get_max(bank)
    if first_pos == len(bank) - 1:
        first_max, first_pos = get_max(bank[:-1])
    
    second_max, second_pos = get_max(bank[first_pos + 1:])

    total += int(first_max + second_max)
    
print(total)