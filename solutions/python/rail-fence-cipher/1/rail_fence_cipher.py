from itertools import chain, cycle


def rail_assigner(message, rails):
    row = [None for i in range(len(message))]
    grid = [row.copy() for i in range(rails)]
    for index, cycle_step in enumerate(cycle(chain(range(0, rails - 1, 1), range(rails - 1, 0, -1)))):
        if index == len(message):
            break
        else:
            grid[cycle_step][index] = message[index]
    return grid

def rail_creator(encoded_message, rails):
    row = [None for i in range(len(encoded_message))]
    grid = [row.copy() for i in range(rails)]
    for index, cycle_step in enumerate(cycle(chain(range(0, rails - 1, 1), range(rails - 1, 0, -1)))):
        if index == len(encoded_message):
            break
        else:
            grid[cycle_step][index] = 1
    return grid


def list_cutter(list, number):
    for i in range(0, len(list), int(len(list) / number)):
        yield list[i:i + int((len(list) / number))]


def encode(message, rails):
    output = []
    for row in rail_assigner(message, rails):
        output.append(list(filter(None, row)))
    return ''.join(list(chain.from_iterable(output)))


def decode(encoded_message, rails):
    output = []
    iterator = iter(list(encoded_message))
    grid = list(chain.from_iterable(rail_creator(encoded_message, rails)))
    for index, value in enumerate(grid):
        if value == 1:
            grid[index] = next(iterator)
  #  return list(list_cutter(grid, rails))
    for index, cycle_step in enumerate(cycle(chain(range(0, rails - 1, 1), range(rails - 1, 0, -1)))):
        if index == len(encoded_message):
            break
        else:
            output.append(list(list_cutter(grid, rails))[cycle_step][index])
    return ''.join(output)
    
    