from sys import argv
from csv import *
from re import *

def main():
    test_process_tweet_text("Lol, k. â€œ@JetBlue: Our fleet's on fleek. http://t.co/IUX94Rgc83	neutral")
    test_process_tweet_text("JetBlue's CEO battles to appease passengers and Wall Street - Waterbury Republican American http://t.co/5t4FpCGREJ	neutral")
    test_process_tweet_text("Lol, k. â€œ@JetBlue: Our fleet's on fleek. http://t.co/IUX94Rgc83 Don't be like the other airlines!!  http://t.co/WHAGPknnLF	negative")
    # pass
    process_input_files()

def process_input_files():
    # get file names
    training_file = argv[1]
    testing_file = argv[2]

    # read files(\t delimiter)
    training_data_set = read_training_file(training_file)
    testing_date_set = read_testing_file(testing_file)
    
    # process tweet texts
    training_data_set["tweet_texts"] = process_tweet_texts(training_data_set["tweet_texts"])
    testing_date_set["tweet_texts"] = process_tweet_texts(testing_date_set["tweet_texts"])
    

def read_training_file(file_name):
    data_set = dict()
    instance_numbers = list()
    tweet_texts = list()
    sentiments = list()
    with open(file_name) as tsv_file:
        tsv_reader = reader(tsv_file, delimiter = '\t')
        for row in tsv_reader:
            instance_numbers.append(row[0])
            tweet_texts.append(row[1])
            sentiments.append(row[2])
    data_set["instance_numbers"] = instance_numbers
    data_set["tweet_texts"] = tweet_texts
    data_set["sentiments"] = sentiments
    return data_set

def read_testing_file(file_name):
    data_set = dict()
    instance_numbers = list()
    tweet_texts = list()
    with open(file_name) as tsv_file:
        tsv_reader = reader(tsv_file, delimiter = '\t')
        for row in tsv_reader:
            instance_numbers.append(row[0])
            tweet_texts.append(row[1])
    data_set["instance_numbers"] = instance_numbers
    data_set["tweet_texts"] = tweet_texts
    return data_set

def process_tweet_texts(tweet_texts):
    processed_tweet_texts = list()
    for tweet_text in tweet_texts:
        # remove url
        tweet_text = sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"," ",tweet_text)
        # remove junk characters
        tweet_text = sub(r"[^#@_$%\sa-zA-Z\d]","",tweet_text)
        # add process tweet
        process_tweet_texts.append(tweet_text)
    return processed_tweet_texts


if __name__ == '__main__':
    main()   