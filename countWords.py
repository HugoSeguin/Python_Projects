#oal is to count the number of words in a paragraph in file name

def wordcount(filename):
    counts = ('characters':0,'words': 0,'lines': 0)
    unique_words = set()

    for one_line in open (filename):
        counts['lines'] +=1
        counts['characters'] += len(one_line)
        counts['words'] += len(one_line.split())

        unique_words.update(oneline.split())

    counts['unique words'] = len(unique_words)
    for key, value in counts.items():
        print(f'{key}: {value}')

wordcount('wcfile.txt')
    