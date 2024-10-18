class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        all_words = {}
        tmp_words = str()
        f_chars = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in range(len(self.file_names)):
            with open(self.file_names[i], encoding='utf-8') as file:
                for line in file:
                    tmp_words += line.lower()
                for j in f_chars:
                    tmp_words = tmp_words.replace(j, ' ')
            all_words[self.file_names[i]] = tmp_words.split()
            tmp_words = str()
        return all_words

    def find(self, word):
        res_d_f = {}
        for k, v in self.get_all_words().items():
            for i in range(len(v)):
                if str(word).lower() == v[i]:
                    res_d_f[k] = i + 1
                    break
        return res_d_f

    def count(self, word):
        res_d_c = {}
        for k, v in self.get_all_words().items():
            col = 0
            for i in range(len(v)):
                if str(word).lower() == v[i]:
                    col += 1
            res_d_c[k] = col
        return res_d_c

if __name__ == '__main__':

    finder1 = WordsFinder('test_file.txt', 'second_file.txt')
    print(finder1.file_names)
    print(finder1.get_all_words())
    print(finder1.find('TEXT'))
    print(finder1.count('tEXT'))
    print('\n')

    finder2 = WordsFinder('Mother Goose - Monday’s Child.txt', )
    print(finder2.get_all_words())
    print(finder2.find('Child'))
    print(finder2.count('Child'))
    print('\n')

    finder3 = WordsFinder('Rudyard Kipling - If.txt', )
    print(finder3.get_all_words())
    print(finder3.find('if'))
    print(finder3.count('if'))
    print('\n')

    finder4 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(finder4.get_all_words())
    print(finder4.find('captain'))
    print(finder4.count('captain'))