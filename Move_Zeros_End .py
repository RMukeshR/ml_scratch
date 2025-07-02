#Move Zeros to the End of the List


class Move_zero:
    def __init__(self,arr):
        self.arr = arr

    def move_zero(self):
        for i in self.arr:
            if i== 0:
                self.arr.remove(i)
                self.arr.append(0)
        
        return self.arr
    

arr = list(map(int, input("""Enter list element sep by " " - """).strip().split()))

mov = Move_zero(arr)

print(mov.move_zero())