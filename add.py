# 1st Tutorial about strings and number
'Bucky Ribert'
'I don\'t like it'
print('C:\Bucky\Window\ndtv') # it sdee as \n so it changes line 
print(r'C:\Bucky\Window\ndtv') # It treat as string with no spical items
firstName = 'Bucky '
print(firstName + 'Robert')
print(firstName * 5)

# 2nd Tutorial about Slicing up String
user = 'Tuna McFish'
user[0] #Left to right
user[5]
user[-1] # Right to left
user[-3]
user[2:7] # Slicing the string starts at user[2] and ends at user[7]
user[:7] # Slice the string start at user[0] ends at user[7]
user[2:] # Slice the string start at user[2] endds at the end
user[:] # Slice from start to end

len('asasasaas') # Give us the length of the string

# Tutorial 3rd about Lists

players = [29, 24, 38]
players + [90,91, 98] # adding in list but don;t change the list permanent
players.append(120) # adding the item permanet
players[:2] 
players[:2] = [0, 0] # Replace multiple item at sametime
players[:2] = [] # Removing the item from list