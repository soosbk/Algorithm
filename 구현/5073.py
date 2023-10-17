

while True:
    idx=list(map(int,input().split()))
    if idx.count(0)==3: break
    if idx[0]>=idx[1]+idx[2] or idx[1]>=idx[0]+idx[2] or idx[2]>=idx[1]+idx[0]: 
            print("Invalid")
            continue

    if idx[0]==idx[1] and idx[1]== idx[2]: 
        print("Equilateral")
    elif idx[0]==idx[1] or idx[1]==idx[2] or idx[0]==idx[2]:
        print("Isosceles")

    else:
        print("Scalene")

