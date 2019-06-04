def move(player, direction):
    x, y, hp = player
    if direction == (-1, 0) and x > 0:
        x -= 1
    elif direction == (1, 0) and x < 4:
        x += 1
    elif direction == (0, -1) and y > 0:
        y -= 1
    elif direction == (0, 1) and y < 4:
        y += 1
    else:
        hp -= 5        
        
        
    return x, y, hp

print(move((0, 1, 10), (-1, 0)))