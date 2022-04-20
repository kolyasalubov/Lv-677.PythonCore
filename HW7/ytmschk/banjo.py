def are_you_playing_banjo(name):
    if name.find('R') == 0 or name.find('r') == 0:
        return f'{name} plays banjo'
    else:
        return f'{name} does not play banjo'