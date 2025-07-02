#Largest Element


class Find_largest:
    def __init__(self,n):
        self.n = n

    def find_large(self):
        lar = self.n[0]

        for i in self.n:
            if i > lar:
                lar = i
        return lar
    
    def find_2nd_lar(self):
        lar = float("-inf")

        lar2 = float("-inf")

        
    
arr = list(map(int,input("""Enter element sep by " " """ ).strip().split(" ")))

fin_lar = Find_largest(arr)

print(fin_lar.find_large())
