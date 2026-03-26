unit=int(input())
if unit>=1 and unit<=10:
    p=5*unit
elif unit>=11 and unit<=50:
    p=7*(unit-10)+50
elif unit>=51 and unit<=100:
    p=10*(unit-50)+330
elif unit>=101 and unit<=200:
    p=12*(unit-100)+830
else:
    p=15*(unit-200)+2030
ft=unit*0.50
print(f"{(p+(p*0.07)+ft):.2f}")