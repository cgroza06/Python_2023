def compose(musical_notes, moves, start_pos):
    song = []
    song.append(musical_notes[start_pos])
    for i in moves:
        start_pos += i
        song.append(musical_notes[start_pos])
    return song

musical_notes = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Si"]
input_moves = input("Introdu miscarile, separata de un spatiu: ")
input_moves = input_moves.split()
moves = []
for i in input_moves:
    moves.append(int(i))
start_pos = int(input("Introduceti pozitia de inceput: "))

result = compose(musical_notes,moves,start_pos)
print(result)
