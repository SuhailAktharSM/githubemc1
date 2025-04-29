s = [1,1,22,23]

for x in s:
    for y in s:
        for z in s:
            for u in s:
                l = [x,y,z,u]
                if l.count(1) == 2 and l.count(22)==1 and l.count(23) == 1: 
                    if (x-y)*z+u == 24:
                        print(f"({x}-{y})*{z}+{u}")
                    elif (y-x)*z+u == 24:
                        print(f"({y}-{x})*{z}+{u}")
                    elif x-(y*z)+u == 24:
                        print(f"{x}-({y}*{z})+{u}")
                    elif (y*z)+u-x == 24:
                        print(f"({y}*{z})+{u}-{x}")
                    elif y*(z+u)-x == 24:
                        print(f"{y}*({z}+{u})-{x}")
                    elif x- y*(z+u) == 24:
                        print(f"{x}-{y}*({z}+{u})")
print("hello")
print("Iron Man")