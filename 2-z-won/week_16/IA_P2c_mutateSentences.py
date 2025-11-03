def mutateSentences(sentence):
    """
    High-level idea: generate sentences similar to a given sentence.
    Given a sentence (sequence of words), return a list of all possible
    alternative sentences of the same length, where each pair of adjacent words
    also occurs in the original sentence. (The words within each pair should appear
    in the same order in the output sentence as they did in the orignal sentence.)
    Notes:
    - The order of the sentences you output doesn't matter.
    - You must not output duplicates.
    - Your generated sentence can use a word in the original sentence more than
      once.
    """
    # BEGIN_YOUR_CODE (our solution is 20 lines of code, but don't worry if you deviate from this)
    from collections import defaultdict

    words = sentence.split()
    n = len(words)
    if n == 0:
        return []
    succ = defaultdict(set)
    for i in range(n - 1):
        succ[words[i]].add(words[i + 1])

    def make_node(w):
        return {w: set(succ.get(w, ()))}

    def word_of(node):
        return next(iter(node.keys()))

    def neighbors(node):
        next_words = next(iter(node.values()))
        return [make_node(nw) for nw in next_words]

    results = set()

    if n == 1:
        return list({words[0]}) if words else []

    def dfs(path_nodes):
        if len(path_nodes) == n:
            sent = " ".join(word_of(nd) for nd in path_nodes)
            results.add(sent)
            return
        
        for nxt in neighbors(path_nodes[-1]):
            path_nodes.append(nxt)
            dfs(path_nodes)
            path_nodes.pop()

    for start_w in list(succ.keys()):
        dfs([make_node(start_w)])

    return list(results)

    # END_YOUR_CODE