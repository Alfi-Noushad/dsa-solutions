def pascalTriangle():
    prev = [1]
    print(prev)
    for i in range(4): 
        curr = [1]        #5row
        for j in range(len(prev)-1):
            curr.append(prev[j]+prev[j+1])
        curr.append(1)
        print(curr)
        prev = curr
    
pascalTriangle()