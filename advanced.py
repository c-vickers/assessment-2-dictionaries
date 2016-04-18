"""Advanced skills-dictionaries.

  IMPORTANT: these problems are meant to be solved using dictionaries and sets.
"""


def top_characters(input_string):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example:

        >>> top_characters("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:

        >>> top_characters("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    letter_count = {}

    #Build letter count dictionary
    for letter in input_string:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    #Compare values -- still not sure how to do the list to a list thing. 
    # for count, letter in letter_count.items:
    #     high_count = 0
    #     if count > high_count:
    #         high_count = [count]
    #     elif count ==


    return []


def adv_alpha_sort_by_word_length(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """
    alpha_dict = {}

    #create dictionary
    for word in words:
        if len(word) in alpha_dict:
            alpha_dict[len(word)].append(word)
        else:
            alpha_dict[len(word)] = [word]

    for item in alpha_dict:
        alpha_dict[item] = sorted(alpha_dict[item])

    #sort dictionary
    sorted_alpha_set = sorted(alpha_dict.iteritems())

    return sorted_alpha_set


##############################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
