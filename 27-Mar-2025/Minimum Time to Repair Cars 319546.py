# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        r=cars*cars*max(ranks)
        l=1
        def valid(mid):
            car=0
            for i  in ranks:
                car+=floor(sqrt(mid/i))
            return car>=cars
        while r>=l:
            mid=(l+r)//2
            f=valid(mid)
            if valid(mid):
                r=mid-1
            else:
                l=mid+1
        return l
                     