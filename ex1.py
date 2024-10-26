def palindrome_star(n):
    for i in range(1, n + 1):
        print(" " * (n - i))
        print("* " * i)
        
    for i in range(n - 1, 0, -1):
        print(" " * (n - i))
        print("* " * i)

rows = int(input())
palindrome_star(rows)