v=0
x=0
def setup():
    size(1000,1000)
def draw():
    global x,v
    for v in range(10):
        global x
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        rect(v,v,x,x)
        v=v+100
        x=x+1
