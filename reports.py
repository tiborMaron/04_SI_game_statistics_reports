import os


# Report functions


# Reads the file to a 2D list, and returns it
def read_file(file_name):
    games = []
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    file = open(file_name)
    for line in file:
        games.append(line.split("\t"))
    file.close()
    for game in games:
        game[4] = game[4][:-1]
    return games


# How many games are in the file?
def count_games(file_name):
    games = read_file(file_name)
    return len(games)


# Is there a game from a given year?
def decide(file_name, year):
    games = read_file(file_name)
    for game in games:
        if game[2] == str(year):
            return True
    return False


# Which was the latest game?
def get_latest(file_name):
    games = read_file(file_name)
    latestGame = ["", 0]
    for game in games:
        if int(game[2]) > latestGame[1]:
            latestGame[0] = game[0]
            latestGame[1] = int(game[2])
    return latestGame[0]


# How many games do we have by genre?
def count_by_genre(file_name, genre):
    games = read_file(file_name)
    count = 0
    for game in games:
        if game[3] == genre:
            count += 1
    return count


# What is the line number of the given game (by title)?
def get_line_number_by_title(file_name, title):
    games = read_file(file_name)
    for index, game in enumerate(games):
        if game[0] == title:
            return index + 1
    raise ValueError


# What is the alphabetical ordered list of the titles?
def sort_abc(file_name):

    # Read the file
    games = read_file(file_name)

    # Init list with the first game's name
    sortedTitles = []
    sortedTitles.append(games[0][0])

    # Go through the games
    for game in range(1, len(games)):

        # Lower than the first in the list
        if games[game][0] < sortedTitles[0]:
            sortedTitles.insert(0, games[game][0])
            continue

        # Higher than the last in the list
        if games[game][0] > sortedTitles[-1]:
            sortedTitles.append(games[game][0])
            continue

        # Is between the first and the last
        for idx, title in enumerate(sortedTitles):
            if games[game][0] > title and games[game][0] < sortedTitles[idx + 1]:
                sortedTitles.insert(idx + 1, games[game][0])
                break

    # Return the list
    return sortedTitles


# What are the genres?
def get_genres(file_name):
    games = read_file(file_name)
    genres = []
    for game in games:
        if game[3] not in genres:
            genres.append(game[3])
    genres = sorted(genres)
    return genres


# What is the release date of the top sold "First-person shooter" game?
def when_was_top_sold_fps(file_name):
    games = read_file(file_name)
    topSold = [0, 0]
    for game in games:
        if game[3] == "First-person shooter":
            if float(game[1]) > float(topSold[0]):
                topSold[0] = float(game[1])
                topSold[1] = game[2]
    return int(topSold[1])
