# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
def are_you_playing_banjo(name):
    # Implement me!
    isStartWith = name.startswith(('R', 'r'))
    if isStartWith:
        result = name + ' plays banjo'
    else:
        result = name + ' does not play banjo'
    return result

case = are_you_playing_banjo('Ramen')
print(case)