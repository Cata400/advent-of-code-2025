def check_id(id: int) -> bool:
    id_str = str(id)
    no_digits = len(id_str)
    
    for div in range(2, no_digits+1):
        if no_digits % div != 0:
            continue
        
        string_divisions = [id_str[i * no_digits // div: (i + 1) * no_digits // div ] for i in range(div)]
        
        truths = [1]
        for i in range(1, len(string_divisions)):
            truths.append(int(string_divisions[i] == string_divisions[i-1]))
        
        if sum(truths) == len(truths): 
            return True
        
    return False


ids = open('input.txt', 'r').read().replace('\n', '') # for the last element
ranges = ids.split(',')

invalids = 0
for id_range in ranges:
    first, last = id_range.split('-')
    first, last = int(first), int(last)
    
    for id in range(first, last + 1):
        if check_id(id): invalids += id
        
print(invalids)