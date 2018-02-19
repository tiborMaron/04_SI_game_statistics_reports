import os
import math

TITLE = 0
SOLD = 1
RELEASE = 2
GENRE = 3
PUBLISHER = 4


# Reads the file to a 2D list, and returns it
def read_file(file_name):
    games = []
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    file = open(file_name)
    for line in file:
        games.append(line.split("\t"))
    file.close()
    for game in games:
        game[PUBLISHER] = game[PUBLISHER][:-1]
    return games


# What is the title of the most played game (i.e. sold the most copies)?
def get_most_played(file_name):
    games = read_file(file_name)
    max_copies_sold = 0
    index = 0
    for idx, game in enumerate(games):
        if float(game[SOLD]) > max_copies_sold:
            max_copies_sold = float(game[SOLD])
            index = idx
    return games[index][TITLE]


# How many copies have been sold total?
def sum_sold(file_name):
    games = read_file(file_name)
    total_sold = 0
    for game in games:
        total_sold += float(game[SOLD])
    return total_sold


# What is the average selling?
def get_selling_avg(file_name):
    games = read_file(file_name)
    return sum_sold(file_name) / len(games)


# How many characters long is the longest title?
def count_longest_title(file_name):
    games = read_file(file_name)
    max_chars = 0
    for game in games:
        if len(game[TITLE]) > max_chars:
            max_chars = len(game[TITLE])
    return max_chars


# What is the average of the release dates?
def get_date_avg(file_name):
    games = read_file(file_name)
    total_years = 0
    for game in games:
        total_years += int(game[RELEASE])
    return math.ceil(total_years / len(games))


# What properties has a game?
def get_game(file_name, title):
    games = read_file(file_name)
    the_game = []
    for game in games:
        if game[TITLE] == title:
            the_game.append(game[TITLE])
            the_game.append(float(game[SOLD]))
            the_game.append(int(game[RELEASE]))
            the_game.append(game[GENRE])
            the_game.append(game[PUBLISHER])
            return the_game


# How many games are there grouped by genre?
def count_grouped_by_genre(file_name):
    games = read_file(file_name)
    count_by_genres = {}
    for game in games:
        if game[GENRE] not in count_by_genres:
            count_by_genres[game[GENRE]] = 1
        else:
            count_by_genres[game[GENRE]] += 1
    return count_by_genres


# What is the date ordered list of the games?
def get_date_ordered(file_name):
    games = sorted(read_file(file_name))
    titles = []
    while len(games) != 0:
        max_year = games[0][RELEASE]
        max_year_index = 0
        for idx, game in enumerate(games):
            if game[RELEASE] > max_year:
                max_year = game[RELEASE]
                max_year_index = idx
        titles.append(games[max_year_index][TITLE])
        del games[max_year_index]
    return titles
