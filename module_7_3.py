import io
from pprint import pprint


class WordFinder:
    def __init__(self, *args):
        self.file_names = args


    def get_all_words(self):
        all_words = dict()
        i = 0
        while i < len(self.file_names):
            name = self.file_names[i]
            with open(name, encoding='utf-8') as file:
                a = list()
                for line in file:
                    b = line
                    punctuation_marks = [',', '.', '!', '?', '-', ':', ';']
                    for j in punctuation_marks:
                        b = b.replace(j, '')
                    a += (b.lower()).split()
            all_words.update({self.file_names[i]:a})
            i += 1
        return all_words


    def find(self, word):
        i = 0
        res_find = dict()
        while i < len(self.file_names):
            name = self.file_names[i]
            all_words_name = self.get_all_words()[name]

            j = 0
            while j <  len(all_words_name):
                if all_words_name[j] == word.lower():
                    res_find.update({name: j+1})
                    break
                j +=1
            i += 1
        return res_find

    def count(self,word):
        i = 0
        res_count = dict()
        while i < len(self.file_names):
            name = self.file_names[i]
            all_words_name = self.get_all_words()[name]

            j = 0
            count = 0
            while j < len(all_words_name):
                if all_words_name[j] == word.lower():
                    count += 1
                j += 1
            res_count.update({name:count})
            i += 1
        return res_count





wf = WordFinder('O Captain! My Captain!.txt', 'if.txt', 'Monday’s Child.txt')
print(wf.find('the'))
print(wf.count('the'))