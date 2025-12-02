ids = open('input.txt', 'r').read().replace('\n', '') # for the last element
ranges = ids.split(',')

invalids = 0
for id_range in ranges:
    first, last = id_range.split('-')
    first, last = int(first), int(last)
    
    for id in range(first, last + 1):
        id_str = str(id)
        no_digits = len(id_str)
        
        if no_digits % 2 == 1:
            continue
        
        if id_str[:no_digits // 2] == id_str[no_digits // 2:]:
            invalids += id
        
print(invalids)