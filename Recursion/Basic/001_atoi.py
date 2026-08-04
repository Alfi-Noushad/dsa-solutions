s = "123"
lenght = len(s)
def atoi(index,current):
    if index == lenght:
        return current

    digit = int(s[index])

    newcurrent = current * 10 + digit

    return atoi(index+1,newcurrent)

print(atoi(0,0))
