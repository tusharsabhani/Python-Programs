n=int(input())
for k in range(n):
    word=input()
    l=len(word)
    if l>10:
        print(word[0]+str(l-2)+word[l-1])
    else:
        print(word)
