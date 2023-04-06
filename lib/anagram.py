class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        result = [word for word in words if sorted([letter for letter in self.word]) == sorted([letter for letter in word])]
        return result