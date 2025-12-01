rotations = open('input.txt', 'r').readlines()
rotations = [rotation.replace('\n', '') for rotation in rotations]
print(rotations)

position = 50
password = 0

for rotation in rotations:
    direction, magnitude = rotation[0], int(rotation[1:])
    
    if direction == 'L':
        magnitude = -magnitude
    
    position += magnitude
    position %= 100
    
    if position == 0: password += 1
    
print(password)