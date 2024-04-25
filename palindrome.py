def palindrome(n):
    return n==n[::-1]
n=input("enter the text")
ans=palindrome(n)
if ans:
    print("yes")
else:
    print("false")
