import datetime


class Censore:

    def __init__(self) -> None:
        self.find_bad_words = []
        self.bad_words = self._load_bad_words()

    def _load_bad_words(self) -> list:
        """
            load bad words from file
        """
        with open("full_bad_list.txt") as f:
            list_of_words = f.read()
            return list_of_words.split("\n")

    def _alone_words(self, string: str) -> None:
        """
            if word just wrote like "alone". It will detecte it!
            Before: "Fuck man"
            After: "**** man"
        """
        string_strip = string.split()

        for item in string_strip:
            if item in self.bad_words:
                self.find_bad_words.append(item)

    def _deep_filter(self, string: str) -> None:
        """
            if word masking near another words, this function will detecte it!
            Before: "Fuckyou"
            After:  "****you"
        """
        # Deep filter
        for word in self.bad_words:
            i = 0
            for _ in string:
                if not len(word) > len(string):
                    if string[i:len(word) + i] in self.bad_words:
                        self.find_bad_words.append(
                            string[i:len(word) + i])
                    i += 1

    def censore(
        self,
        string: str,
        custom_words: list = None,
        masking_symbol: str = "*"
    ) -> str:
        if custom_words is not None:
            for word in custom_words:
                self.bad_words.append(word)

        self._alone_words(string.lower())
        self._deep_filter(string.lower())
        # Replace word to masking_symbol
        for word in self.find_bad_words:
            string = string.replace(word, masking_symbol * len(word))

        return string


if __name__ == "__main__":
    """
        If you want to add you own custom word:
        cen.censore("Your own string".lower(), ["Your custom word", "a lot of your own words"])
    """
    start = datetime.datetime.now()
    cen = Censore()
    print("Load file --", datetime.datetime.now() - start)

    cen = cen.censore("A peace of shit")
    print("Detecte words --", datetime.datetime.now() - start)
    # A peace of ****

    print(cen)
