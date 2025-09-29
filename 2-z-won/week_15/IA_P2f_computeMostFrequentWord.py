def computeMostFrequentWord(text):
    """
    Splits the string |text| by whitespace and returns two things as a pair:
        the set of words that occur the maximum number of times, and
    their count, i.e.
    (set of words that occur the most number of times, that maximum number/count)
    You might find it useful to use collections.defaultdict(float).
    """
    # BEGIN_YOUR_CODE (our solution is 5 lines of code, but don't worry if you deviate from this)
    from collections import defaultdict
    count_dict = defaultdict(int)
    for word in text.split(): count_dict[word] += 1
    most_count = max(count_dict.values())
    return (set(word for word, count in count_dict.items() if count == most_count), most_count)
    # END_YOUR_CODE