import math
a,b,c=input().split(" ")
a,b,c=int(a),int(b),int(c)
if(a+b+c>=3):print(math.trunc(0.9*(a*25+b*40+c*55)))
else:print(a*25+b*40+c*55)