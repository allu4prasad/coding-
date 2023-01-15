
def countLetters(S):
    total = 1
    count = 1
    comb=[]
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            comb.append(S[:i])
            count += 1
        else:
            count = 1
            comb.append(S[:i])
        total += count
    return total,comb
