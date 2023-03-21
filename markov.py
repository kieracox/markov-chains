"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    # file variable, set as opening the argument
    file = open(file_path)
    # text variable, reading the file and printing out a string
    text = file.read()
    file.close()
    return text

   


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    #split the input text string by spaces to get a list of all words
    words = text_string.split()
    # Set as kind of a stopping point, so that we know when we've reached the last key
    words.append(None)
    # loop through the words list, stopping at 1 before the last so we dont get an index error
    for i in range(len(words) - 2):
       # key and value variables: key is a tuple of the word at current index and the one after; value is the word after that
       key = (words[i], words[i + 1])
       value = words[i + 2]
        # add the key to our dictionary, the value is set to an empty list. then we append the value to that list
       if key not in chains:
           chains[key] = []
    
       chains[key].append(value)
        
    
    return chains
    


   


def make_text(chains):
    """Return text from chains."""

    # create a link (a random key from our dict) in the form of list
    key = choice(list(chains.keys()))
    # add words from the key we've selected to a list
    words = [key[0], key[1]]
    # random choice from the values of key we've selected
    new_word = choice(chains[key])

    #loop through all the words while we aren't at the None placeholder
    while new_word is not None:
        #make a new link: second word of previous link + new_word
        key = (key[1], new_word)
        #add the new word to words list
        words.append(new_word)
        #get another word
        new_word = choice(chains[key])


    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
