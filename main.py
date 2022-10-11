def anagram_checker(word1, word2):
    word1 = ''.join(word1.lower().split())
    word2 = ''.join(word2.lower().split())

    if len(word1) != len(word2):
        return False

    return sorted(word1) == sorted(word2)


# Test Cases
print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
