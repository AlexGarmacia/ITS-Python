def count_isolated(lst: list) -> int:
    count = 0
    
    for i in range(len(lst)):
        
        if (i == 0 or lst[i] != lst[i - 1]) and (i == len(lst) - 1 or lst[i] != lst[i + 1]):
            count += 1
    
    return count
