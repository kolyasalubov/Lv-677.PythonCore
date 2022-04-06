def are_you_playing_banjo(name):
    name = name.strip()
    return f"{name} plays banjo" if name[0] == "R" or name[0] == "r" else f"{name} does not play banjo"
