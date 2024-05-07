"""This program counts the number of word occurrences in a text file,
then it prints the top x words with counts"""

import string

# open the text file to analyse
text = open("test_file.txt", "r").read()
# create a dictionary for words
word_count_dict = dict()

# create a list for stop words
stop_word_list= []
# open the stop word text file
stop_word_file = open("italian_stop_words.txt", "r")
# load all stop words in the list stop_word_list
stop_word_text =  stop_word_file.read()
for stop_word in stop_word_text.split():
    stop_word_list.append(stop_word)

# change the text to be analysed to lowercase to avoid case mismatch
text = text.lower()

# remove unwanted chars (i.e. all chars except {a, ..., z} and {à, è, é, ì, ò, ù})
unwanted_char_list = list(string.ascii_lowercase + "àèéìòù")
clean_text = ""
for char in text:
    # add the char if it is not included in the unwanted set, otherwise add a whitespace
    if char in unwanted_char_list:
        clean_text = clean_text + char
    else:
        clean_text = clean_text + " "

# split into words (spliting is based on withespaces)
words = clean_text.split()
# for each word in text:
for word in words:
    # removes stop word and numeric words
    if word not in stop_word_list:
        # check if the word is already in dictionary
        if word in word_count_dict:
            # increment count of word by 1
            word_count_dict[word] = word_count_dict[word] + 1
        else:
            # add the word to dictionary with count 1
            word_count_dict[word] = 1

# print top x words sorted by count
top_x = 20
word_count_list_sorted = sorted(word_count_dict.items(), key=lambda kv: kv[1])
print("Top", top_x, " words:")
for i, elem in enumerate(reversed(word_count_list_sorted)) :
    print(elem[0], "->", elem[1])
    if i == top_x:
        break

