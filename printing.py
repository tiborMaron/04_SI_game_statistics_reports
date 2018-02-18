from reports import *


# Printing functions


def print_count_games(file_name):
    print(count_games(file_name))


def print_decide(file_name):
    print(decide(file_name, input("Which year? ")))


def print_get_latest(file_name):
    print(get_latest(file_name))


def print_count_by_genre(file_name):
    print(count_by_genre(file_name, input("What genre? ")))


def print_get_line_number_by_title(file_name):
    print(get_line_number_by_title(file_name, input("Title? ")))


def print_sort_abc(file_name):
    sortedGames = sort_abc(file_name)
    for item in sortedGames:
        print(item)


def print_get_genres(file_name):
    genres = get_genres(file_name)
    for genre in genres:
        print(genre)


def print_when_was_top_sold_fps(file_name):
    print(when_was_top_sold_fps(file_name))


def main():
    file_name = input("Filename? ")

    # Basic questions
    print_count_games(file_name)
    print_decide(file_name)
    print_get_latest(file_name)
    print_count_by_genre(file_name)
    print_get_line_number_by_title(file_name)

    # Bonus questions
    print_sort_abc(file_name)
    print_get_genres(file_name)
    print_when_was_top_sold_fps(file_name)


if __name__ == "__main__":
    main()
