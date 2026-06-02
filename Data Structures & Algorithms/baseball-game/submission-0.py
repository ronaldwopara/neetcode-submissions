class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []
        for i in range(len(operations)):
            try:
                res.append(int(operations[i]))
            except ValueError:
                if operations[i] == "+":
                    res.append(res[-1] + res[-2])
                if operations[i] == "C":
                    res.pop(-1)
                if operations[i] == "D":
                    res.append(res[-1]*2)
        return sum(res)


        




       



                


                
            

        