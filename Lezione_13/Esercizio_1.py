def recusirvePower(b:int,e:int) -> int:
    if e == 0:
        return 1
    else:
        return b * recusirvePower(b,e-1) 
    
RecursivePower = recusirvePower(3,4)
print(RecursivePower)
RecursivePower = recusirvePower(4,3)
print(RecursivePower)
RecursivePower = recusirvePower(2,5)
print(RecursivePower)
RecursivePower = recusirvePower(5,2)
print(RecursivePower)