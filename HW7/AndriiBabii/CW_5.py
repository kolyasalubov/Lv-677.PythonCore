#https://www.codewars.com/kata/are-you-playing-banjo

def are_you_playing_banjo(name):
    if name.startswith("r") or name.startswith("R"): return name + " plays banjo" 
    else: return name + " does not play banjo"
