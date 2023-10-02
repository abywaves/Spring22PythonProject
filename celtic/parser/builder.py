""""builder functions

This module has functions for populating dictionaries from different containers
"""

import parser as pa

# *************************************************
# Dictionaries for storing data from the text files.
# *************************************************

# This is a dictionary where the
# Key -> document name
# Value -> List of all words in that document
corpus_data = {}

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document
doc_word_index = {}

# This is a dictionary where the
# Key -> word in corpus
# Value -> the total number of times that word appears in the corpus
global_count_index = {}

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of words in the document
word_count_index = {}

# This is a dictionary where the
# Key -> document name
# Value -> another dictionary, where:
#     Key -> word in document
#     Value -> number of times that word appears on that document / total number of unique words in that document
weighted_word_count_index = {}

# This is a dictionary where the
# Key -> word in the corpus
# Value -> list with names of all documents where that word appears
doc_inverted_index = {}

# This is a dictionary where the
# Key -> document name
# Value -> list of unique words in document
doc_dictionary = {}

# This is a dictionary where the
# Key -> word in corpus,
# Value -> logarithm in base 10 of (total number of documents in corpus / number of documents containing that word)
adjusted_index = {}

# *************************************************
# Functions
# *************************************************
# Builds the doc_word_index dictionary by using another container as
# argument on the parameter data
# Don't modify this function
def build_doc_word_index(data):
    temp_dictionary = {}
    for document, words_list in data.items():
        inner_dictionary = {}

        for word in words_list:
            if word in inner_dictionary:
                inner_dictionary[word] += 1
            else:
                inner_dictionary[word] = 1

        temp_dictionary[document] = inner_dictionary

    return temp_dictionary

# Builds the global_count_index dictionary by using another container as
# argument on the parameter data
# Don't modify this function
def build_global_count_index(data):
    temp_dictionary = {}
    for document, words_list in data.items():
        for word in words_list:
            if word in temp_dictionary:
                temp_dictionary[word] += 1
            else:
                temp_dictionary[word] = 1
    return temp_dictionary


# Builds the word_count_index dictionary by using another container as
# argument on the parameter data
def build_word_count_index(data):
    temp_dictionary = {}
    word_count = []
    for document, words_list in data.items():
        inner_dictionary = {}

        for word in words_list:
            if word in inner_dictionary:
                inner_dictionary[word] += 1/len(word)
            else:
                inner_dictionary[word] = 1/len(word)

        temp_dictionary[document] = inner_dictionary

    return temp_dictionary

# Builds the weighted_word_count_index dictionary by using another container as
# argument on the parameter data
def build_weighted_word_count_index(data):
    temp_dictionary = {}
    uniquewords = []
    for document, words_list in data.items():
        inner_dictionary = {}

        for word in words_list:
            if word in inner_dictionary:
                inner_dictionary[word] += 1/len(uniquewords)
            else:
                inner_dictionary[word] = 1/len(uniquewords)

        temp_dictionary[document] = inner_dictionary

    return temp_dictionary

# Builds the doc_inverted_index dictionary by using another container as
# argument on the parameter data
def build_doc_inverted_index(data):
    temp_dictionary = {}
    inverted_index = {}
    wordCount = {}
    for documents,words_list in data.items():
        for word in words_list.lower().split():
            wordCount[word] = wordCount.get(word, 0)+1
            if inverted_index.get(word, False):
                if documents in inverted_index[word]:
                    inverted_index[word].append(documents)
            else:
                inverted_index[word] = [documents]

    return temp_dictionary

# Builds the doc_dictionary dictionary by using another container as
# argument on the parameter data
def build_doc_dictionary(data):
    temp_dictionary = {}
    uniqueWords = []
    uniqueWords.append(data.items[0])
    for documents in range(len(data.items)):
        for word_list in range(len(data.items)):
            if data.items[documents] == uniqueWords[word_list]:
                break
        else:
            uniqueWords.append(data.items[documents])
            print(uniqueWords)

    return temp_dictionary


# Builds the adjusted_index dictionary by using another container as
# argument on the parameter data
def build_adjusted_index(data):
    temp_dictionary = {}
    import math

    for documents, words_list in data.items:
        inner_dictionary = {}

        for word in words_list:
            if word in inner_dictionary:
                inner_dictionary[documents] = math.log()

        temp_dictionary = inner_dictionary[documents]

    return temp_dictionary

