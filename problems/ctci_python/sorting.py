class Sorting:
    def __init__(self):
        pass

    """
    Problem 1:
    Given a string, word, consisting of lowercase letters only, return a sorted array with all the letters in word sorted from most frequent to least frequent. 
    If two frequencies are the same, break the tie alphabetically.

    Example 1: word = "supercalifragilisticexpialidocious"
    Output: ['i', 'a', 'c', 'l', 's', 'e', 'o', 'p', 'r', 'u', 'd', 'f', 'g', 't',
    'x']

    -> Calculate frequencies for each character
    -> Sort the freq_dict based on the count for each value
    -> Need to support lexicographically if the character count is a tie

    Example 2: word = "aabbbcccc"
    Output: ['c', 'b', 'a']. 'c' appears 4 times, 'b' appears 3 times, and 'a'
    appears 2 times.

    Example 3: word = "abc"
    Output: ['a', 'b', 'c']. All letters appear once, so they are sorted
    alphabetically.
    """

    def letter_occurences(self, word):
        ch_freq = {}

        for ch in word:
            ch_freq[ch] = ch_freq.get(ch, 0) + 1

        print(ch_freq)

        # sort based on the count and the lexicographical order. This can be done using a tuple
        # return the array in sorted order. If there is a tie in count lexicographically
        
        tuples = sorted(ch_freq.items(), key=lambda x: (-x[1], x[0]))
        print(tuples)

        return [x for x, _ in tuples]


    """
    Problem 31.2 - Nested Circles
    Determine if circles are nested (one surrounds all others recursively).

    Input: Array of circles [((x, y), r), ...] (center coordinates + radius)
    Output: Boolean - are circles nested?
    Examples:

    circles = [((4, 4), 5), ((8, 4), 2)] → false (neither contains the other)
    circles = [((5, 3), 3), ((5, 3), 2), ((4, 4), 5)] → true (outermost contains all)
    circles = [((5, 3), 3)] → true (single circle counts as nested)


    Constraints: len(circles) ≤ 10^4, coordinates/radii are integers [-10^4, 10^4]
    """

    def nested_circles(self, circles):
        pass


    """
    You're given an array of n integers, nums, and another array of at most n integers, operations, where each integer represents an operation to be performed on nums.

    If the operation number is k ≥ 0, the operation is "delete the number at index k in the original array if it has not been deleted yet. Otherwise, do nothing."
    If the operation number is -1, the operation is "delete the smallest number in nums that has not been deleted yet, breaking ties by smaller index."
    
    Return the state of nums after applying all the operations. Every number in operations is guaranteed to be between -1 and n-1 inclusive.
    
    nums = [50, 30, 70, 20, 80]
    operations = [2, -1, 4, -1]

    if positive, delete the number at index k in the original array if it has been not deleted yet. otherwise do nothing.
    if negative, delete the smallest number that has not been deleted yet, breaking ties by smaller index


    enumerated_nums = [(0, 50), (1, 30), (2, 70), (3, 20), (4, 80)]

    """

    



if __name__ == "__main__":
    s = Sorting()

    word = "supercalifragilisticexpialidocious"
    print(s.letter_occurences(word))

