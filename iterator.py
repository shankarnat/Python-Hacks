import re

RE_WORD = re.compile('\w+')

class Sentence:
    def __init__(self, sent):
        self.sent = sent
        self.words = RE_WORD.findall(sent)

    def __len__(self):
        return len(self.words)

    def __getitem__(self, index):
        return self.words[index]


class SentIter:
    def __init__(self, sent):
        self.sent = sent
        self.words = RE_WORD.findall(sent)

    def __iter__(self):
        for s in self.words:
            yield s
        return

if __name__ == '__main__':
    sentobj = Sentence("Hello World")
    it = iter(sentobj)
    print(next(it))
    sentob1 = SentIter("Hello World")
    obj = iter(sentob1)
    print(list(obj))
