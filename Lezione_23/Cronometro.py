def cronometro(fun):
    def wrapper():
        import time
        start = time.time()
        fun()
        print(time.time()-start)
    return wrapper

@cronometro
def prova():
    for i in range(1000000):
        pass 

print(prova)



