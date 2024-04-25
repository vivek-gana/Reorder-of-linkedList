even_number=0
odd_number=0
number=int(input("enter the number you want:"))
while number!=0:
    if number%2==1:
        odd_number+=1
    else:
        even_number+=1
    number=int(input("enter second number:"))
print(even_number)
print(odd_number)
    

