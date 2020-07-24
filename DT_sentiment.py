from sys import argv
from csv import *
from re import *

def main():
    process_input_files()
    pass

def process_input_files():
    # Get file names
    training_file = argv[1]
    testing_file = argv[2]

    # Read files(\t delimiter)
    training_data_set = read_training_file(training_file)
    testing_date_set = read_testing_file(testing_file)

def read_training_file(file_name):
    data_set = dict()
    instance_number = list()
    tweet_text = list()
    sentiment = list()
    with open(file_name) as tsv_file:
        tsv_reader = reader(tsv_file, delimiter = '\t')
        for row in tsv_reader:
            instance_number.append(row[0])
            tweet_text.append(row[1])
            sentiment.append(row[2])
    data_set["instance_number"] = instance_number
    data_set["tweet_text"] = tweet_text
    data_set["sentiment"] = sentiment
    return data_set

def read_testing_file(file_name):
    data_set = dict()
    instance_number = list()
    tweet_text = list()
    with open(file_name) as tsv_file:
        tsv_reader = reader(tsv_file, delimiter = '\t')
        for row in tsv_reader:
            instance_number.append(row[0])
            tweet_text.append(row[1])
    data_set["instance_number"] = instance_number
    data_set["tweet_text"] = tweet_text
    return data_set


if __name__ == '__main__':
    main()   