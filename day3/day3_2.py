def get_max(arr):
    arr = [int(x) for x in arr]
    maxim = max(arr)
    position = arr.index(maxim)
    
    return str(maxim), position


banks = open('input.txt', 'r').readlines()
banks = [rotation.replace('\n', '') for rotation in banks]

total = 0
no_batteries = 12
for bank in banks:
    jolts = []
    start = 0
    for i in range(no_batteries):   
        limit = len(bank) - no_batteries + i + 1
        maxim, pos = get_max(bank[start:limit])

        jolts.append(maxim)
        
        start += pos + 1

    total += int("".join(jolts))
    
print(total)