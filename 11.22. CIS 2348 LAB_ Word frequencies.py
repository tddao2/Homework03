#Tri Dao
#1954347
#11.22 CIS 2348 LAB: Word frequencies

inp = input()
words = inp.split()
wordEmpty = []
for wordIndex in words:
    wordEmpty.append(str(wordIndex))
for pos, val in enumerate(wordEmpty):
    print('{} {}'.format(val, wordEmpty.count(wordEmpty[pos])))
    
    