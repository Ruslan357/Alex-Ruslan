
fin = open('mobi.txt')
line = fin.readline()
for line in fin:
    word = line.strip()
    i = 0
    k = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            k = k + 1
            if k == 3:
                print (word)
            i = i + 2
        else:
            i = i + 1 - 2*k
            k = 0

    



