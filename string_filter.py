import datetime
from typing import Union


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

    def _filter(self, string: str) -> None:
        """
            if word just wrote like "alone" or near other words. It will detecte it!
            Before: "Fuck manshit"
            After: "**** man****"
        """
        for word in self.bad_words:
            if word in string:
                self.find_bad_words.append(word)

    def censore(
        self,
        string: str,
        custom_words: Union[list, None] = None,
        masking_symbol: str = "*"
    ) -> str:
        if custom_words is not None:
            for word in custom_words:
                self.bad_words.append(word)

        self._filter(string.lower())
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

    start = datetime.datetime.now()
    censor = cen.censore("A peace of shit")
    print("Detecte words --", datetime.datetime.now() - start)
    # A peace of ****
    print(censor)
