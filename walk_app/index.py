# Envia um array contendo uma letra representando uma direção
# Sempre anda um bloco por letra e leva 1 minuto para atravessar qualquer um deles.
# Deve levar dez minutos a caminhada e ele deve sempre retornar para o ponto de origem.

def increment_north(point):
    
    new_point = [point[0] + 1, point[1]]

    return new_point

def increment_south(point):
        
    new_point = [point[0] - 1, point[1]]

    return new_point

def increment_east(point):

    new_point = [point[0], point[1] + 1]

    return new_point

def increment_west(point):

    new_point = [point[0], point[1] - 1]

    return new_point

def increment(point, direction):

    north = increment_north
    south = increment_south
    west = increment_west
    east = increment_east

    dict_incremention = dict({
        'n': north,
        's': south,
        'w': west,
        'e': east
    })

    return dict_incremention[direction](point)

def is_valid_walk(walk):
    
    qtd_minutes = len(walk)

    if qtd_minutes != 10:
        return False

    point_origin = [0, 0]

    point = point_origin

    for direction in walk:

        point = increment(point, direction)

    if point == point_origin:
        return True
    
    return False


