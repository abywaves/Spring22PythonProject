"""stats functions

This module computes some statistics from the text corpus
"""

# Returns the number of times the most common word appears in the corpus, the parameter
# data is a container to be used for such task
def most_common_word(data):
    print('most_common_word: ', end='')
    # use python built in max() function to get the key with the maximum value and store the value in word as a string
    # get returns the key
    word = max(data, key=data.get)
    # use variable count to store the value of the key stored in word
    count = data[word]
    # return tuple with word and count
    return (word, count)


# Returns the document with the highest number of words
# If the second parameter is not given (the default)
# returns the document with the highest number of unique words
# data is a container to be used for such task
def get_largest_document(data, unique=False):
    print('get_largest_document: ', end='')
    size = 0
    set = 0
    document = ''
    largestdocument = {}
    uniqueset = {}
    if unique == True:
        for i in data:
            size = sum(data[i].values())
            largestdocument.update({i:size})
            document = max(largestdocument, key=largestdocument.get)
    else:
         for i in data:
             set = len(data[i].keys())
             uniqueset.update({i:set})
             document = max(uniqueset, key=uniqueset.get)

    return document


# Returns the average length of the words in a document
# the parameter data is a container to be used for such task
# the parameter document is the name of the document (string)
def avg_length(data, document):
    print('avg_length: ' + document + ': ',  end='')

    count = 1
    total = 0
    for i in data:
        total = sum(data[i].values())
        count = len(data[i].keys())

    return total / count


# Returns a list with all words in the corpus that end with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter
def get_words_letter_end(data, letter):
    print('get_word_letter_end: ' + letter + ': ', end='')
    words = []
    wordlist = []

    for i in data.values():
        wordlist = wordlist + i

    for j in wordlist:
        if j.endswith(letter):
            words.append(j)

    return words


# Returns a list with all words in the corpus that begin with a given letter
# the parameter data is a container to be used for such task
# the parameter letter is a string, indicating the letter
def get_words_letter_begin(data, letter):
    print('get_word_letter_begin: ' + letter + ': ', end='')
    words = []

    wordlist = []

    for i in data.values():
        wordlist = wordlist + i

    for j in wordlist:
        if j.startswith(letter):
            words.append(j)

    return words


# Returns a list with all words in the corpus of a given size
# the parameter data is a container to be used for such task
# the parameter size is an integer, indicating the size
def get_words_size(data, size):
    print('get_word_size: ' + str(size) + ': ', end='')
    words = []
    wordlist = []

    for i in data.values():
        wordlist = wordlist + i

    for j in wordlist:
        if len(j) == size:
            words.append(j)

    return words


# computes the average size of words in the corpus
# the parameter data is a container to be used for such task
def compute_avg(data):
    print('compute_avg: ', end='')
    avg = 0.0
    wordlist = []
    divisor = 0
    total = 0
    for i in data.values():
        wordlist = wordlist + i

    for j in wordlist:
        total += len(j)

    divisor = len(wordlist)

    avg = total/divisor

    return avg


# Returns a list with all words in the corpus whose size is greater than
# the corpus words average size
def get_words_grater_avg(data, avg_size):
    print('get_words_grater_avg: ', end='')
    words = []
    wordlist = []

    for i in data.values():
        wordlist = wordlist + i

    for j in wordlist:
        if len(j) > avg_size:
            words.append(j)

    return words

