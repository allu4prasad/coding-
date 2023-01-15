def polindrome_check(s):
    res=set()
    for i in s:
        if i not in res:
            res.add(i)
        else:
            res.remove(i)
    return len(res)<=1
