def mixColor(c1,c2):return (c1+c2)//2
def mixRGB(r1,g1,b1,r2,g2,b2):
    rMix=mixColor(r1,r2)
    gMix=mixColor(g1,g2)
    bMix=mixColor(b1,b2)
    return rMix,gMix,bMix
r1,g1,b1=map(int,input().split(" "))
r2,g2,b2=map(int,input().split(" "))
a,b,c=mixRGB(r1,g1,b1,r2,g2,b2)
print(a,b,c)