def break_words(stuff):
    """this function will break up words for us"""
    words= stuff.split(' ')
    return words
	
def sort_words(words):
    """sorts the words"""
    return sorted(words)
	
def print_first_word(words):
    """Print the first word after popping it off."""
    word= words.pop(0)
    print word
	
def print_last_word(words):
    """Prints the last word after popping it off."""
    word= words.pop(-1)
    print word
	
def sort_sentence(sentence):
    """ take in a full sentance and return the sorted words."""
    words=break_words(sentance)
    return sort_words(words)
	
def print_first_and_last(sentance):
    """print the first and last words of the sentance"""
    words=break_words(sentance)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentance):
    """Sorted the words then prints the first and last one."""
    words=sort_sentence(sentance)
    print_first_word(words)
    print_last_word(words)


print "lets see what happen here"
x= open("test1.txt")
y= x.read()

print "sorting"

z= sort_words(y)
print z 
