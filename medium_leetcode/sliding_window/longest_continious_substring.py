def longest_cont_substring(s):
    start=0
    max_len=0
    char_dict={}
    results=""
    for end,c in enumerate(s):
        if c in char_dict:
            start=char_dict[c]+1
        char_dict[c]=end
        if end-start+1>max_len:
            max_len=end-start+1
            results=s[start:end+1]
    return results
s = "abcabcdbb"
print(longest_cont_substring(s))
