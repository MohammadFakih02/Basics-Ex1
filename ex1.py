def palindrome_star(n):
    for i in range(1, n + 1):
        print(" " * (n - i),end="")
        print("* " * i)
        
    for i in range(n - 1, 0, -1):
        print(" " * (n - i),end="")
        print("* " * i)


rows = int(input(" enter number of rows "))
palindrome_star(rows)