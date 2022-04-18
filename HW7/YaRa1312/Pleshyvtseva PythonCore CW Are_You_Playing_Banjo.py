# CodeWars Are_You_Playing_Banjo_?

def are_you_playing_banjo(name):
    name = name.strip()
    if name[0] == "R" or name[0] == "r":
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"
    # Implement me!
