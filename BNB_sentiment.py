from sys import argv
from csv import *
from re import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

def main():
    # process input files
    data_sets = process_input_files()
    training_data_set = data_sets[0]
    testing_data_set = data_sets[1]

    # create count vectorizer and fit it with training data
    count = CountVectorizer(token_pattern="[a-zA-Z0-9\#\@\_\$\%]{2,}",lowercase=False)
    train_bag_of_words = count.fit_transform(training_data_set["tweet_texts"])

    # transform the test data into bag of words creaed with fit_transform
    test_bag_of_words = count.transform(testing_data_set["tweet_texts"])

    # BNB model
    clf = BernoulliNB()
    model = clf.fit(train_bag_of_words, training_data_set["sentiments"])

    # predict
    predicted = model.predict(test_bag_of_words)

    # print result
    for i in range(len(testing_data_set["tweet_texts"])):
        print(testing_data_set["instance_numbers"][i],predicted[i])


def process_input_files():
    # get file names
    training_file = argv[1]
    testing_file = argv[2]

    # read files(\t delimiter)
    training_data_set = read_training_file(training_file)
    testing_data_set = read_testing_file(testing_file)
    
    # process tweet texts
    training_data_set["tweet_texts"] = process_tweet_texts(training_data_set["tweet_texts"])
    testing_data_set["tweet_texts"] = process_tweet_texts(testing_data_set["tweet_texts"])
    return (training_data_set,testing_data_set)

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
    clean_tweet_texts = list()
    for tweet_text in tweet_texts:
        # remove url
        tweet_text = sub(r"http[s]?:\/\/\S+"," ",tweet_text)
        # remove junk characters
        tweet_text = sub(r"[^a-zA-Z0-9\s\#\@\_\$\%]","",tweet_text)
        # append clean tweet text to list
        clean_tweet_texts.append(tweet_text)
    return clean_tweet_texts


if __name__ == '__main__':
    main()   