class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        scores={}
        for ID,score in items:
            if ID in scores:
                scores[ID].append(score)
            else:
                scores[ID]=[score]
        results=[]
        for I in scores:
            student_scores=scores[I]
            student_scores.sort(reverse=True)
            student_scores=student_scores[:5]
            top_5_avg=sum(student_scores)//5
            results.append([I,top_5_avg])
        results.sort(key=lambda x:x[0])
        return results
