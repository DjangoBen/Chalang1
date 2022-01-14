def direction(facing, turn):
    direction = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turn_count = (turn%360)//45
    if (direction.index(facing))+1+turn_count <= 8:
        return direction[direction.index(facing)+turn_count]
    else:
        flag = 7-direction.index(facing)
        turn_count -= flag
        return direction[turn_count-1]