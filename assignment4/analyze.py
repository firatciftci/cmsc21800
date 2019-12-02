from core import *
import datetime

def match():
    '''
    Match must return a list of tuples of amazon ids and google ids.
    For example:
    [('b000jz4hqo', http://www.google.com/base/feeds/snippets/11125907881740407428'),....]

    '''

    #YOUR CODE GOES HERE

    return []

#prints out the accuracy
now = datetime.datetime.now()
out = eval_matching(match())
timing = (datetime.datetime.now()-now).total_seconds()
print("----Accuracy----")
print(out)
print("---- Timing ----")
print(timing,"seconds")