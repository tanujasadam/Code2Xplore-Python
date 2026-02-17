n=int(input("Enter number of weights:"))
weights=[]
for i in range(n):
    weights.append(int(input("Enter weight:")))
print("Weights entered:", weights)
very_light=[]
normal_load=[]
heavy_load=[]
overload=[]
invalid_entries=[]

valid_entries=0

for w in weights:
    if w<0:
        invalid_entries = invalid_entries + [w]
    elif w<=5:
        very_light = very_light + [w]
        valid_entries += 1
    elif w<=25:
        normal_load = normal_load + [w]
        valid_entries += 1
    elif w<=60:
        heavy_load = heavy_load + [w]
        valid_entries += 1
    else:
        overload = overload + [w]
        valid_entries += 1



