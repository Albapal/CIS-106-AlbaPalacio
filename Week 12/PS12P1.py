items = []

# DL1
print("Step 1 Create list **********")
arraylength =int(input("Number of Items : "))
for i in range(arraylength):
    item =int(input("Value : "))
    items.append(item)

print(items)

# DL2
print("Step 2 Insert value **********")
items.insert(0, 99)

print(items)

# DL3
print("Step 3 Update value **********")
items[0] = 100

print(items)

# DL4
print("Step 4 Extend lists **********")

items2 = [500,600,700,800,900]
print(items2)

items.extend(items2)
print(items)

# DL5
print("Step 5 Remove item by value **********")
items.remove(800)
print(items)

# DL6
print("Step 5 Remove item by index **********")
items.pop(2)
print(items)

# DL7
print("Step 7 Create list Grades **********")
grades = ["A","B","C","A","A","C"]
print(grades)

# DL8
print("Step 8 Count Grades **********")
quant = grades.count("A")
print(quant)

# DL9
print("Step 9 Display Index **********")
quant = grades.index("B")
print(quant)

# DL10
print("Step 10 Look for not valid value **********")
if "F" not in grades:
    print(f"Value 'F' is not in the list")

# DL11
print("Step 11 Clear list **********")
items2.clear()
print(items2)

# DL12
print("Step 11 Delete list **********")
del items2
#print(items2)

# DL13
print("Step 13 Create list Players **********")
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print(players)

# DL14
print("Step 14 Sort list **********")
players.sort()
print(players)

# DL15
print("Step 15 Copy list **********")
players2 = []
players2 = players.copy()
print(players2)

# DL16
print("Step 16 Reverse list **********")
players2.reverse()
print(players2)