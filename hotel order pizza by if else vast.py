size=input("enter the size of pizza(S/M/L)")
bill=0
if size=='s' or size=='S':
    bill +=100
    print("the small pizzza price is 100 RS")
elif size =='m' or size =='M':
    bill +=200
    print("the medium pizzza price is 200 RS")
else:
    bill +=300
    print("the large pizzza price is 300 RS")
add_pepperoni=input("do you want to add pepperoni (Y/N)?")
if 'add_papperoni' =='Y' or'add_papperoni' =='y':
    if size =='S' or size=='s':
        bill+=30
else:
    bill=50

extra_cheese=input("do  you want extra cheese(Y/N)?")
if extra_cheese=='Y' or extra_cheese=='y':
    bill+=20

print(f"your final bill is {bill}")




