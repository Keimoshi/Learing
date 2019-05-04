def make_great(magicians,great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magicians.append("The Great Magician " + magician)
    return great_magicians

def show_magicians(great_magicians):
    while great_magicians:
        magician = great_magicians.pop()
        print(magician)