def build_profile(first_name:str, last_name:str, **kwargs): 
#kwargs= serve per inserire più argomenti di quelli definiti

    output= f"{first_name} {last_name}," 

    for key, value in kwargs.items():
        output += f"{key} {value},"

    return output


output = build_profile("eric","Crown", age=45, hair="brown", weight=72, height=180)
print(output)
