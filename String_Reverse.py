class StringReverse:
    def __init__(self, text):
        self.__text = text    

    def reverse_words(self):
        words = self.__text.split()
        return " ".join(words[::-1])

    def __str__(self):
        return self.reverse_words()


s = StringReverse("Python is very easy")
print(s)