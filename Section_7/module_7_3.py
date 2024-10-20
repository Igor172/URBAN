class WordsFinder:
    def __init__(self, *files):
        self.file_names = list(files)
        self.all_words = {}

    def get_all_words(self):
        for file_name in self.file_names:
            words_list = []
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for char in "',.=!?:;-":
                        text = text.replace(char, ' ')
                    words = text.split()
                    words_list.extend(words)
            except FileNotFoundError:
                print(f"File '{file_name}' not found.")
            self.all_words[file_name] = words_list
        return self.all_words

    def find(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            if word in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word)
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))