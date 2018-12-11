import sys
from io import StringIO


class prefix(object):
    def __init__(self):
        self.word_list = []
        self.m = 0
        self.n = 0
        self.buffer = StringIO()

    def get_wordlist(self):
        sys.stdout.write('Input:\n')
        line = input()
        self.n, self.m = (int(x) for x in line.split())
        for i in range(self.n):
            raw_word = input()
            if raw_word == '\n':
                break
            if len(raw_word.split()) == 2:
                act, word = (x for x in raw_word.split())
            if len(raw_word.split()) == 1:
                act = raw_word.split()[0]
                print(act)

            if act == '1':
                self.buffer.seek(0, 2)
                self.buffer.write(word)
                print(self.buffer.getvalue())
            elif act == '2':
                self.buffer.seek(0, 2)
                temp = self.buffer.getvalue()
                self.buffer.truncate(0)
                self.buffer.write(temp[:-1])
                print(self.buffer.getvalue())
            elif act == '3':
                self.word_list.append(self.buffer.getvalue())
                print(self.word_list)
            else:
                break
        self.buffer.close()

    def find_prefix(self, prefix):
        frequency = 0
        sub_list = []
        for i in self.word_list:
            if i.startswith(prefix):
                sub_list.append(i)
                frequency = frequency+1
        return frequency, sub_list

    def search_prefix(self):
        sys.stdout.write('Search:\n')
        for i in range(self.m):
            prefix = input()
            if prefix =='\n':
                break
            frequency, sub_list = self.find_prefix(prefix)
            print("{", end="")
            print(*sub_list, sep=",", end="")
            print("}", "total:", frequency)


def main():
    p = prefix()
    p.get_wordlist()
    p.search_prefix()

if __name__ == '__main__':
    main()