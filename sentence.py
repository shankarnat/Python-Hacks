import reprlib
import re

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self,index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

if __name__ == "__main__":
    sent = Sentence("Hello World")
    y = iter(sent)
    print(next(y))
