sentence = "This film is best film of the year"
find = 'film'
replaceWith = 'movie'

words=sentence.split(' ')

for i in range(0,len(words)):
    if words[i]==find:
        words[i]=replaceWith

print(' '.join(words))