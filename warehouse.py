"""
    Program: Warehouse management system
    Functionality:
       - Repeted menu
       - Register items to the catalog
            id(auto generated)
            title
            category
            price
            stock
        -Display Catalog
        -Display items with no stock (out of stock)

"""
from menu import menu, clear, header
from item import Item

#global vars
catalog = []

#functions
def register_item():
    """ clear()
    print("-" * 30)
    print(" Register New Item")
    print("-" * 30) """
    
    header(" Register new Item")

    title= input("New item title:    ")
    category = input ("New item category:   ")
    price= float(input ("New item price:   "))
    stock= int(input("New Item stock:    "))

    new_item = Item() #Create instances of a class (objects)
    new_item.id= 0
    new_item.title= title
    new_item.category= category
    new_item.price= price
    new_item.stock= stock

    catalog.append(new_item)
    print("Item created!")

def display_catalog():
    """ clear()
    print("-" *30)
    print("Current Catalog")
    print("-" *30) """
    """print("there are: "+ str(size) + "items") """
    
    size= len(catalog)
    header("Current Catalog ("+ str(size) + "items)")

    #print("-" * 70)
     print("|" +'ID'.rjust(2)
        + "|" + 'Title'.ljust(20)
        + "|" + 'Category'.ljust(15)
        + "|" + 'Price'.rjust(10)
        + "|" + 'Stock'.rjust(5)+ "|")
        print("-" * 70)

for item in catalog:
    print("|" + str(item.id).rjust(2)
     + "|" + item.title.ljust(24)
     + "|" + item.category.ljust(15)
     + "|" + str(item.price).rjust(10)
     + "|" + str(item.stock.rjust(5)+ "|")

     print("-" * 70)

def display_not_stock():
    size= len(catalog)
    header("Out of stock (" + str(size) + " items)")

    #print("-" *70)
        print("|" +'ID'.rjust(2)
        + "|" + 'Title'.ljust(24)
        + "|" + 'Category'.rjust(15)
        + "|" + 'price'.rjust(10)
        + "|" + 'Stock'.rjust(5)+ "|")
    print("-" * 70)

    for item in catalog:
        if(item.stock == 0):
        print
        ("|" + str(item.id).rjust(2)
        + "|" + item.title.ljust(20)
        + "|" + item.category.ljust(15)
        + "|" + str(item.price.rjust(10)
        + "|" + str(item.stock).rjust(5)+ "|")

    print("-" * 70 )

#instructions
#start menu
opc = ''
while(opc !='x'):
    clear()
    menu()
    print("/n")
    opc=input("please select an option: ..")

    if(opc=='1'):
        register_item()
    elif(opc=='2'):
        display_catalog()
    elif (opc == '3'):
        display_no_stock()

    input ("Press enter to continue...")