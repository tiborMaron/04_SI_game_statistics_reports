from reports import *


# What is the title of the most played game (i.e. sold the most copies)?
def print_get_most_played(file_name):
    print(get_most_played(file_name))


# How many copies have been sold total?
def print_sum_sold(file_name):
    print("{0:.2f}".format(sum_sold(file_name)))


# What is the average selling?
def print_get_selling_avg(file_name):
    print("{0:.2f}".format(get_selling_avg(file_name)))


# How many characters long is the longest title?
def print_count_longest_title(file_name):
    print(count_longest_title(file_name))


# What is the average of the release dates?
def print_get_date_avg(file_name):
    print("{0:.0f}".format(get_date_avg(file_name)))


# What properties has a game?
def print_get_game(file_name, title):
    game = get_game(file_name, title)
    print("{0}: {1} million copies sold, released in {2}. Genre: {3}. Publisher: {4}.".format(
        game[TITLE], game[SOLD], game[RELEASE], game[GENRE], game[PUBLISHER]
    ))


# How many games are there grouped by genre?
def print_count_grouped_by_genre(file_name):
    genres = count_grouped_by_genre(file_name)
    for key, value in genres.items():
        print("{0}: {1} title.".format(key, value))


# What is the date ordered list of the games?
def print_get_date_ordered(file_name):
    titles = get_date_ordered(file_name)
    for title in titles:
        print(title)


def main():
    file_name = input("Filename: ")

    # Basic questions
    print_get_most_played(file_name)
    print_sum_sold(file_name)
    print_get_selling_avg(file_name)
    print_count_longest_title(file_name)
    print_get_date_avg(file_name)
    print_get_game(file_name, input("Title? "))

    # Bonus questions
    print_count_grouped_by_genre(file_name)
    print_get_date_ordered(file_name)


if __name__ == "__main__":
    main()
