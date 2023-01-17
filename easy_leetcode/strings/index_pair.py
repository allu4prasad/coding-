
class Solution(object):
    def indexPairs(self, text, words):
        results=[]
        for i in words:
            start=0
            while start<len(text):
                start=text.find(i,start)
                if start==-1:
                    break
                results.append([start,start+len(i)-1])
                start+=1
        return (sorted(results))
