rotations = open('input.txt', 'r').readlines()
rotations = [rotation.replace('\n', '') for rotation in rotations]

position = 50
password = 0

for rotation in rotations:
    direction, magnitude = rotation[0], int(rotation[1:])
    
    if direction == 'L':
        magnitude = -magnitude
    
    position_prev = position
    position += magnitude
        
    # The circle has not completed a rotation passing through 0
    if 0 < position < 100 or (position_prev == 0 and -100 < position < 0):
        position %= 100
        continue
    
    # The dial stops exactly on 0
    elif position == 0: 
        password += 1
    
    # The dial passes through the right
    elif position >= 100:
        password += position // 100
    
    # The dial passes through the left, not starting from 0 
    if position_prev != 0 and position < 0:
        password += abs(position // 100)
        if position % 100 == 0:
            password += 1
    
    # The dial passes through the left, starting from 0   
    elif position_prev == 0 and position < 0:
        password += (abs(position // 100) - 1)
        if position % 100 == 0:
            password += 1
    

    position %= 100
    
print(password)
