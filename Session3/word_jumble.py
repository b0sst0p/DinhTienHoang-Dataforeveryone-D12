from random import shuffle, randint #hoac dung choice
word = 'champion, winner,loser'
list_word = list(word)
# another_list_word = word.split(',')
shuffle(list_word)
# print(list_word)
# print(another_list_word)
# temp = list_word[0] 
# list_word [0] = list_word [1]
# list_word[1] = temp
# print(list_word)
for char in list_word:
    print(char,end='')
