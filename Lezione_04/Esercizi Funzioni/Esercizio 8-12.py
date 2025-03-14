def sandwich(*args):
    print("il suo sandwich è composto da: ") 
    for ingrediente in args:
         print(f"{ingrediente}")

sandwich("salame","formaggio")
sandwich("cotoletta","maionese","formaggio","pane")
