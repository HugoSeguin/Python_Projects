#Pig Latin
#Split so find first letter
#if begin with vowel tan add way to end of word, append()
def pl_setence(sentence):
    output = []
    if word[0] in 'aeiou':
        output.append(f'{word}way')
    else:
        output.append(f'{word[1:]}{word[0]}ay')
return ' '.join(output)

#if beigns with any other letter thaen take the first letter and put at end of word then add ay, so append()
word = input()
pl_setence(word)
