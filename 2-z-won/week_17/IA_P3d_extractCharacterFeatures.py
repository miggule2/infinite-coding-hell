import random
import collections
import math
import sys
from collections import Counter
from util import *

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''
    def extract(x):
        # BEGIN_YOUR_CODE (our solution is 6 lines of code, but don't worry if you deviate from this)
        s = ''.join(x.split())
        features = {}
        for i in range(len(s) - n + 1):
            ngram = s[i:i+n]
            features[ngram] = features.get(ngram, 0) + 1
        return features
        # END_YOUR_CODE 
    return extract
