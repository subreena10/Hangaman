import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega
    """
    # # word_list = ["navgurukul", "learning", "kindness"]
    # worldlist_filename="words.txt"
    # print("Loading word lidt from file...")
    # inFile=open(worldlist_filename,'r',0)
    # line=inFile.readline()
    # word_list=string.split(line)
    # print(" ",len(word_list),"words loaded.\n")
    with open("/home/sabrina/Desktop/e-sreedharan/hangman/words.txt","r") as word_file:
        a=word_file.read()
        word_list=a.split()
    return word_list

def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()

    return secret_word