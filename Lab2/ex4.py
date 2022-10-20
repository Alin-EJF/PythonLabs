def compose(musicalNotes, moves, start):
    song = []
    song.append(musicalNotes[start])
    for i in range(len(moves)):
        start += moves[i]
        if start >= len(musicalNotes):
            start = start - len(musicalNotes)
        elif start < 0:
            start = len(musicalNotes) + start
        song.append(musicalNotes[start])
    return song


print(compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2))