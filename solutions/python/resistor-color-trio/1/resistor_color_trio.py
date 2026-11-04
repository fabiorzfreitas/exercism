def label(colors):
    color_code = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    ohms = (10 * color_code.index(colors[0]) + color_code.index(colors[1])) * (10 ** color_code.index(colors[2]))
    if ohms >= 1000:
        return f'{int(ohms/1000)} kiloohms'
    else: return f'{ohms} ohms'