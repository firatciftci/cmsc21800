from core import *
import datetime

JACCARD_THRESHOLD = 0.50


def tokenize(st):
    '''
    Takes in a string, converts all characters to lowercase, and tokenizes
    by splitting each individual word

    Returns a new set of tokenized string
    '''
    return set(st.lower().split())


def jaccard(a, b):
    '''
    Given two strings, computes the Jaccard similarity score between them

    Returns the Jaccard similarity score
    '''
    Ta = tokenize(a)
    Tb = tokenize(b)

    return len(Ta.intersection(Tb)) / len(Ta.union(Tb))


def match():
    '''
    Match must return a list of tuples of amazon ids and google ids.
    For example:
    [('b000jz4hqo', http://www.google.com/base/feeds/snippets/11125907881740407428'),....]

    '''
    matches = []
    amazon = amazon_catalog()
    google = google_catalog()

    for i in amazon:
        for j in google:
            if jaccard(i['title'], j['title']) >= JACCARD_THRESHOLD:
                matches.append((i['id'], j['id']))

    return matches


# prints out the accuracy
now = datetime.datetime.now()
out = eval_matching(match())
timing = (datetime.datetime.now() - now).total_seconds()
print("----Accuracy----")
print(out)
print("---- Timing ----")
print(timing, "seconds")
