from hashtable import Hashtable
import time

########################### 
########## Tests ########## 
########################### 

some_words = [u'lewes',          # => 5
              u'mistranscribe',  # => 13
              u'outbleed',       # => 8
              u'abstemiously',   # => 12
              u'antifeudal',     # => 10
              u'tableaux',       # => 8
              u'whine',          # => 5
              u'ytterbite',      # => 9
              u'redeemer']       # => 8

filename = "words.txt"
print(u'Reading words from file {}.'.format(filename))
most_words = []
start_time = time.time()
with open(filename) as f:
    for line in f.readlines():
        most_words.append(line.strip())
print(u'Read in {} words in {}s.'.format(len(most_words), time.time()-start_time))


def do_tests(T):
    """Run the tests for the Hashtable class.

    For the example hashtable, we're mapping strings to integers. More
    specifically, we're mapping words to the number of characters they have,
    just for fun. The test function takes a Hashtable of words mapped to their
    length, and at the end it adds a lot more of them to it.
    """

    print(u'Starting hashtable tests!')
    print(u'#####################')
    print(u'')
    print(u'Initial word list: {}'.format(some_words))
    # test the constructor (which also uses __setitem__ and thereby __getitem__)
    for word in some_words:
        print(u'{} should map to {}.'.format(word, len(word)))
        assert T[word] == len(word)
    print(u'#####################')
    print(u'')



    print(u'Testing __setitem__ and __getitem__')
    # test __setitem__ and __getitem__ some more
    more_words = [u'nummulitic', u'proconviction', u'inscriber']
    print(u'Adding more things to the table: {}'.format(more_words))
    for word in more_words:
        T[word] = len(word)
    # make sure the original words are still there
    for word in some_words:
        print(u'{} should map to {}.'.format(word, len(word)))
        assert T[word] == len(word)
    # make sure the insertion actually worked
    for word in more_words:
        print(u'{} should map to {}.'.format(word, len(word)))
        assert T[word] == len(word)
    print(u'#####################')
    print(u'')
   
   # now delete the second list of words
    print(u'Testing delete')
    for word in more_words:
        print(u'Delete key {}'.format(word))
        del T[word]
    # make sure the words in more_words aren't keys anymore
    keys = T.keys()
    print(u'Current list of keys: {}'.format(keys))
    for word in more_words:
        assert word not in keys
    print(u'#####################')
    print(u'')

    # let's put them back in
    for word in more_words:
        print(u'Re-adding {}.'.format(word))
        T[word] = len(word)
    # make sure the list of keys contains all the words from both lists
    keys = T.keys()
    print(u'Current list of keys: {}'.format(keys))
    for word in some_words:
        assert word in keys
    for word in more_words:
        assert word in keys
    print(u'#####################')
    print(u'')

    print(u'Now, let\'s make the table REALLY big!')
    print(u'(In other words, let\'s test double() and quarter().)')
    print(u'#####################')
    print(u'')

    print(u'Putting a bunch of words in the hashtable.')
    start_time = time.time()
    for word in most_words:
        T[word] = len(word)
    print(u'{} words inserted successfully in {}s.'.format(\
                                                        len(most_words),
                                                        time.time()-start_time))
    print(u'Checking that the words and their values are actually there.')
    for word in most_words:
        l = len(word)
        print(u'{}: {}'.format(word, l))
        assert T[word] == l
    print(u'Deleting a lot of items.')
    for i, key in enumerate(T.keys()):
        if i > 800:
            break
        else:
            del T[key]
    print(u'All tests passed!')
