# Problem: Sort The Students By Their Kth Score - https://leetcode.com/problems/sort-the-students-by-their-kth-score/

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
            # for i  in  range(len(score)):
            #     for  j in range(len(score)-1):
            #         if score[j][k]<score[j+1][k]:
            #             score[j],score[j+1]=score[j+1],score[j]
            # return score
            score.sort(key=lambda s:s[k], reverse=True)
            return score
            
