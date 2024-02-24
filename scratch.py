a=0
b=1
def foo(a):
   return

def bar():
   
   
    if a <= b:
        return foo(a)
    else:
        return foo(b)


    if a > b:
        a,b = b,a
    return foo(a)
