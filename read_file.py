# read_file
# Reads in the data on the players from a csv spreadsheet format
# and restructures it in a helpful way.
# input: a filename
# output: a list of dictionaries with one for each player's stats
# str -> list

def read_file(filename):

    # Open file.
    f = open(filename, 'r')

    # Get the headers for the columns.
    headers = f.readline().strip().split(',')

    # Get all the lines of information from the file.
    lines = f.readlines()

    player_dicts = []
    for line in lines:

        # Split the stats up into a list.
        line = line.strip().split(',')
        # Recombine the first and last names.
        line[1] = line[1] + ',' + line[2]
        # Get rid of the extraneous last name.
        line.remove(line[2])
        # Get rid of extra quotation marks.
        line[1] = line[1][1:-1]
        # Change names to be 'Firstname Lastname' instead of 'Lastname, Firstname'.
        comma = line[1].index(',')
        line[1] = line[1][comma + 2:] + ' ' + line[1][:comma]

        # Convert values that should be ints or floats appropriately.
        for i in range(len(line)):
            if line[i].isnumeric():
                line[i] = int(line[i])
            # Exclude values with the hyphen not as the first character,
            # since those are names.
            elif '-' in line[i] and line[i].find('-') == 0:
                line[i] = int(line[i])
            # Exclude values with spaces, since those are names.
            elif '.' in line[i] and line[i].find(' ') == -1:
                line[i] = float(line[i])
        
        # Initialize a dictionary for each player's stats.
        d = dict()
        for i in range(len(line)):
            d[headers[i]] = line[i]
        player_dicts.append(d)

    f.close()

    return player_dicts
