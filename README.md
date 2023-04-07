# if elif else statement 
age = 13

if age < 21:
    print('No beer for You!')

name = 'Lucyk'

if name == "Bucky":
    print("Hey there Bucky")
elif name == "Lucy":
    print("What up lucedawg!")
else:
    print("Please sign up for the site!")

# Tutorial on for loop

food = ['bacon', 'tuna', 'ham', 'snausages', 'beef']

for i in food[:2]:
    print(i)
    print(len(i))

# Tutorial on Range

for x in range(10):
    print(x)

for x in range(10):
    print('Awesome')

for x in range(5, 12):
    print(x)

for x in range(10, 40, 5):
    print(x)

# Tutorial on while

buttcrack = 5

while buttcrack < 10:
    print(buttcrack)
    buttcrack +=1

# Tutorial on Break 

magicNumber = 26

for n in range(101):
    if n is magicNumber:
        print(n, "is the magic number!")
        break
    else:
        print(n)

# Tutorial on Continue

numbersTaken = [2, 5, 12, 33, 17]

print('Here are the number that are still available:')

for n in range(1,20):
    if n in numbersTaken:
        continue
    print(n)

# Tutorial on Functions

def beef():
    print('Damn, function are cool')

def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)
    
beef()
bitcoin_to_usd(3.85)