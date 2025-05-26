
class comodin:
    pass

def printErr(textoExtra):
    import traceback
    print("\n" + textoExtra + "\n")
    traceback.print_exc()   
import time
secondStart = time.time()
def seconds():
    return time.time()-secondStart
