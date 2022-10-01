#determinar los rebotes 

h=int(input("\n DIgite la altura desde la cual cae la pelota: "))
f= h/5
rebotes=0 

while h>f:
    h=0.9*h
    rebote=rebote+1

print("los rebotes para que la pelota no suba la quinta parte son : "+ str(rebotes))