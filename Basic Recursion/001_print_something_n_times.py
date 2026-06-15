def fun(n):
    if n == 0: 
        return
    
    print(n)

    fun(n-1)
    
    print(n)

fun(5)

#Time Complexity: O(n)
#Space Complexity: O(n)