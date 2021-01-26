
"""Find all word­pair palingrams in a dictionary file."""

import load_dictionary
import time

# We measure the start and end times to find out how long the program takes.
start_time = time.time()

word_list = load_dictionary.load('words.txt')

# Find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end-i]and rev_word[end-i:]in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                if word[:i] == rev_word[end-i:]and rev_word[:end-i]in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list
        
palingrams = find_palingrams()


#sort palingrams on first word
palingrams_sorted = sorted(palingrams)

#display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))	

end_time = time.time()
print(f"Runtime for this program was {end_time -start_time} seconds.")

	