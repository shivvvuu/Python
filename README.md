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

# Tutorial on Return values 

def allowed_dating_age(my_age):
    girls_age = my_age/2 +7
    return girls_age
my_limits = allowed_dating_age(22)
print('I can date ',my_limits,'or older')

# Tutorial on Default Value for Arguments

def get_gender(sex='Unknown'):
    if sex is 'm':
        sex = 'Male'
    elif sex is 'f':
        sex = 'Female'
    print(sex)
    
get_gender('m')
get_gender('f')
get_gender()

# Tutorial on Variable Scope

a = 7823 #global

def corn():
    a= 67 #local
    print(a)
    
def fug():
    print(a)
    
corn()
fug()

# Tutorial on Keyword Argument

def dumb_sentances(name='shivam', action= 'ate', item= 'tuna'):
    print(name, action, item)
    
dumb_sentances()
dumb_sentances('Sailly', 'loves', 'food')
dumb_sentances(item='awesome')
dumb_sentances(item='awesome', action='is')

# Tutorial on Flexible number of Argument

def add_number(*args):
    total = 0
    for i in args:
        total += i
        
    print(total)
    
add_number(3)
add_number(1,5)
add_number(1555,00,55)

# Tutorial on Unpacking Aruments

def health_calculator(age, apple_ate, cig_somked):
    answer = (100-age) + (apple_ate * 3.5) - (cig_somked * 2)
    print(answer)
    
bucky = [27, 20, 0]

health_calculator(bucky[0], bucky[1], bucky[2])
health_calculator(*bucky)

# Tutorial on Sets

groceries = {'cereal' , 'milk', 'starcrunch','beer', 'duct tape', 'beer'}

print(groceries)
 
if 'milk' in groceries:
    print('Yor already have milk in groceries!')
else:
    print('Oh you need to add milk')

# Tutorial on Dictionary

classmates ={'Tony': ' cool but smells', 'Emma': ' sits behine me', 'Lucy': ' asks too many question'}

print(classmates)
print(classmates['Emma'])

for k, v in classmates.items():
    print(k + v)
    
# Tutorial on Modules

import tuna
import random

tuna.fish()

x = random.randrange(1,1000)
print(x)

# Tutorial on Download image from internet

import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + '.jpg' # coverting name into string with str function and adding .jpg to it
    urllib.request.urlretrieve(url, full_name)
    
download_web_image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLkxwzvKdCB7XaYEPRGgu03VFn0YQ-m48r7L7DnLlQXA&s')

# Tutorial on Read and Write on fikle

fw = open('sample.txt', 'w') # create or open file  and with write property
fw.write('Writing some stuff in my text file\n') 
fw.write('I like bacon\n')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
print(text)
fr.close()

# Tutorial on Downloading file from web

from urllib import request

goog_url ='https://support.staffbase.com/hc/en-us/article_attachments/360009197011/username-password-recovery-code.csv' # url of csv file to download

def download_data(csv_url):# function for download csvv file
    response = request.urlopen(csv_url) # Opening the url
    csv = response.read() # Reading from response and storing in csv
    csv_str = str(csv) # converting into string
    lines = csv_str.split("\\n") # Breaking long string into lines
    dest_url = r'goog.csv' # Name of file 
    fx = open(dest_url, 'w') # Making new fike with name
    for line in lines:# Reading the line from lines
        fx.write(line + "\n")# Writing into file which is created
    fx.close() #closing file to free up the memory
    
download_data(goog_url)

# Tutorial on How to build a web crawler

import requests
from bs4 import BeautifulSoup

def trade_spider(max_page):
    page = 1
    while page <= max_page:
        url = 'https://www.ebay.com/b/PC-Laptops-Netbooks/177/bn_317584?_pgn='+str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', { 'class':'s-item__link'}):
            href = link.get('herf')
            title = link.string
            print(href)
            print(title)
            get_single_item_data(href)
        page =+ 1    
        
def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.fineAll('div', 'class':'i-name'):
        print(item_name.string)
    for link in soup.findAll('a'):
        href = link.get('herf')
        print(href)
        

# Tutorial on It's sntax error or u r the only exception

tuna = int(input("what's your fav number:\n"))
print(tuna)

input -> khkhdsfsh #Ecpection Error

tuna = int(inp  ut("what's your fav number:\n")) # Syntax Error
print(tuna)

while True:
    try:
        number = int(input('What\'s your fav number?\n'))
        print(18/number)
        break
    except ValueError:
        print("Make sure and enter a number\n")
    except ZeroDivisionError:
        print("Don't pick zero\n")
    except:
        break
    finally:
        print("loop complete\n")

# Tutorial on Classes and Objects

class Enemy:
    life = 3
    
    def attack(self):
        print('Ouch!')
        self.life -= 1
    def checkLife(self):
        if self.life <= 0:
            print('I am dead')
        else:
            print(str(self.life)+'life left')
            
obj1 = Enemy()
obj2 = Enemy()

obj1.attack()
obj1.attack()
obj2.attack()
obj1.checkLife()
obj2.checkLife()

# Tutorial on init

class Tuna:
    def __init__(self):
        print('Blrrblurlrrer')
    
    def swim(self):
        print('i am swiming!!')
        
obj1 = Tuna()

obj1.swim()

-------------------------------------
class Enemy:
    def __init__(self, x) :
        self.energy = x
        
    def get_energy(self):
        print(self.energy)
        

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()

# Tutorial on Class variable and instance variable

class Girl:
    gender = 'female' #class variable
    
    def __init__(self, name) :
        self.name = name # instance variable
        
r = Girl('Rachel')
s = Girl('Stinky')

print(r.gender)
print(s.gender)
print(r.name)
print(s.name) 

# Tutorial on Inheritance

class Parent():
    def print_last_name(self):
        print('Robert')
        
class Child(Parent): #Inherit
    def print_first_name(self):
        print('Bucky')
    def print_last_name(self): # Override
        print('Snitzleberg')
    
obj = Child()

obj.print_first_name()
obj.print_last_name()

# Tutorial on Multiple Inheritance

class Mario():
    def move(self):
        print('I am moving!')
        
class Shrooms():
    def eat_shrooms(self):
        print("Now I'm big!")
        
class BigMario(Mario, Shrooms):
    pass # Need a line but not to do anything to escape syntax error

obj = BigMario()

obj.move()
obj.eat_shrooms()

# Tutorial on Threading\\

import threading
    
class ShivuMessenger(threading.Thread):
    def run(self):
        for _ in range(10):
            print(threading.currentThread().getName())
            
            
x = ShivuMessenger(name='Send out message')
y = ShivuMessenger(name='Receive message')

x.start()
y.start()

# Tutorial on Word Frequency Counter

import requests
from bs4 import BeautifulSoup
import operator

goog = 'https://www.amazon.in/s?k=the+vertical+mouse&adgrpid=58428791970&ext_vrnc=hi&hvadid=398030099646&hvdev=c&hvlocphy=9146603&hvnetw=g&hvqmt=b&hvrand=718434562865841430&hvtargid=kwd-1126499598474&hydadcr=14339_1999614&tag=googinhydr1-21&ref=pd_sl_6slu5hidaq_b'

def start(url):
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code,features="html5lib")
    for post_text in soup.findAll('span',{'class':'a-size-medium a-color-base a-text-normal'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    clean_up_list(word_list)
    
    
def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = '!@#$%^&*()_+,.";\'<>{}[]:-'
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i],"")
        if len(word) > 0:
            #print(word) 
            clean_word_list.append(word)
    create_dict(clean_word_list)
    
def create_dict(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)

start(goog)

# Tutorial on Unpack List or Tuples

date, name, price = ['December 23,2015', 'Bread Gloves', 8.15]
print(date)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle)/len(middle)
    print(avg)
    
drop_first_last([65,76,98,54,21])

# Tutorial on Zip

first = ['Bucky', 'Tom', 'Taylor']
last = ['Rober', 'Hanks', 'Swift']

names = zip(first, last)

for a, b in names:
    print(a, b)

# Tutorial on Lambda

answer = lambda x: x*7

print(answer(5))

# Tutorial on Min, Max, Sorting Dict

stocks ={
    'GOOG': 520.54,
    'FB':76.45,
    'YHOO':39.28,
    'AMZN':306.21,
    'AAPL':99.76
}

print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))


# Tutorial on Pillow

from PIL import Image

img = Image.open("292.png")
print(img.size)
print(img.format)

img.show()

# Tutorial on Pillow Croping Image

from PIL import Image

img = Image.open("292.png")

area = (100, 100, 120, 120)
cropped_img = img.crop(area)

cropped_img.show()

# Tutorial on Combine Image Together

from PIL import Image

logo = Image.open('292.png')
img = Image.open('99.png')

area = (10, 10, 30, 30)
img.paste(logo, area)

img.show()

# Tutorial on Getting Individual Channel

from PIL import Image

img = Image.open('99.png')

r, g, b, a = img.split()

r.show()
g.show()
b.show()
a.show()

# Tutorial on Merge Effect

from PIL import Image

img = Image.open('99.png')

r, g, b, a = img.split()

new_img = Image.merge('RGBA', (r, g, b, a))

new_img.show()

# Tutorial on Chnageing Mode and filter

from PIL import Image

img = Image.open('99.png')
black_and_white = img.convert('L')

black_and_white.show()
--------------------------------
# Tutorial on Chnageing Mode and filter

from PIL import Image
from PIL import ImageFilter

img = Image.open('99.png')
blur = img.filter(ImageFilter.BLUR)

blur.show()

# Tutorial on Struct

from struct import *

# Store as bytes data
packed_data = pack('iif', 6, 19, 4.73)

print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To get bytes data back to normal

orignal_data = unpack('iif', packed_data)
print(orignal_data)

# Tutorial on map

income = [10, 30, 75]

def double_money(doller):
    return doller * 2

new_income = list(map(double_money, income))

print(new_income)

# Tutorial on bitwise oprator

# ---------BINARY AND--------------

a = 50    # 110010
b = 25    # 011001

c = a & b # 010000

print(c)

# --------------BINARY AND SHIFT---------

x = 240     #11110000
y = x >> 2  # 00111100

print (y)

# Tutorial on Finding Largest or smallest item

import heapq

grade = [32, 43, 654, 34, 132, 66, 99, 532]

print(heapq.nlargest(3, grade))

stock = [
    {'ticker':'AAPL', 'price': 201},
    {'ticker':'GOOG', 'price': 800},
    {'ticker':'F', 'price': 54},
    {'ticker':'MSFT', 'price': 313},
    {'ticker':'TUNA', 'price': 68},
]

print(heapq.nsmallest(2, stock, key= lambda stock: stock['price']))

# Tutorial on Dict Cal

stock = {
   'GGOG': 432,
   'APPL': 325,
   'FB':54,
   'AMAZ': 623,
   'F':32,
   'MSFT':549
}

## with zip (432, GOOG)(325, APPl)

min_price = min(zip(stock.values(), stock.keys()))
print(min_price)

# Tutorial on Find most freq item

from collections import Counter

text = "Southwest Airlines initiated a significant travel disruption that misplaced travelers all across the country."\

"Flights were canceled, re-booking services were temporarily unavailable, and thousands of customers were furious."\

"According to Southwest, the travel interruptions took place between December 24, 2022 and January 2, 2023. However, earlier weather-related flight delays ultimately catapulted the airline into an operational crisis."\

"The most wonderful time of year? Not so much for Southwest."

word = text.split()

counter = Counter(word)
top_three =counter.most_common(3)
print(top_three)

# Tutorial on Dict Multiple Key sort

from operator imnport itemgetter

users = [
    {'fname':'Bucky', 'lname':'Robert'},
    {'fname':'Tom', 'lname':'Robert'},
    {'fname':'Bernie', 'lname':'Zunks'},
    {'fname':'Jenna', 'lname':'Hayes'},
    {'fname':'Sally', 'lname':'Jones'},
    {'fname':'Amanda', 'lname':'Robert'},
    {'fname':'Tom', 'lname':'William'},
    {'fname':'Dean', 'lname':'Hayes'},
    {'fname':'Bernie', 'lname':'Barbie'},
    {'fname':'Tom', 'lname':'Jones'},
]

for x in sorted(users, key=itemgetter('fname')):
    print(x)

print('---------------')
for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)