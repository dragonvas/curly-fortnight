v=0
def setup():
    size(255,255)
def draw():
    global v
    fill(mouseX,mouseX,mouseX)
    for v in 50,100,150,200,250:
        ellipse(50,v,50,50)
        ellipse(50,v,50,50)
        ellipse(50,v,50,50)
        ellipse(50,v,50,50)
        ellipse(50,v,50,50)
    
