def remove_elements(original_set: set[int], elements_to_remove: list[int]) -> set[int]:
    result_set = original_set - set(elements_to_remove)   
    return result_set

print(remove_elements)