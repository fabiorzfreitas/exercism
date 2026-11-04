color_bands = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def value(colors):
    return color_bands.index(colors[0]) * 10 + color_bands.index(colors[1])
