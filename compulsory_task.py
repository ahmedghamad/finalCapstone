import csv # for the csv files 
from tabulate import tabulate #for the tabulate grids
import math # for postive and negative infinties

user_choice = "" # menu empty variable
file_reader_counter = 0 # counter for file reading
shoe_list = [] # empty list that will be used as a list of objects

class Shoes:
    def __init__(self, country, code, product, cost, quantity): # shoe class constructor with its variables
        self.country = country # variable instantiation
        self.code = code # variable instantiation
        self.product = product # variable instantiation
        self.cost = cost # variable instantiation
        self.quantity = quantity # variable instantiation

    def get_cost (self): # cost getter
        return self.cost

    def get_quantity (self): # quantity getter
        return self.quantity

    def set_quantity (self,quantity_input): # quantity setter with quantity input argument
        self.quantity = self.quantity + quantity_input
        return self.quantity

    def __str__(self): # string repersentation
        return (f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}")

    def __repr__(self): # in class converting the member variable to string 
            return (f"{self.country}, {self.code}, {self.product}, {self.cost}, {self.quantity}")   

def update_stock (): # function that updates CSV file 
    header = ['Country', 'Code', 'Product', 'Cost', 'Quantity'] # header for the file
    with open ('inventory.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header) # writes the header to the file
        for line in shoe_list: # for loop that iterates over the shoe list and writes it row by row
            writer.writerow([line.country, line.code, line.product, line.cost, line.quantity])

def read_shoes_data (): # function that reads the input file as CSV
    inventory = [] # inventory list that will be used to creat the shoe object list
    f = None # f value None
    try:
        f = open ('inventory.txt', 'r') # open the file with r mode
        csv_f = csv.reader(f) # CSV reader
        for line in (csv_f): # iterates over every line on the file and adds it to inventory list
            inventory.append(line)
        for line in inventory[1:]: # for loop iterates over the inventory list skip the first line and creats the shoe object list
            shoe = Shoes (line[0],line[1], line[2], int (line[3]), int (line[4])) # creating shoe object with all its variable casted the cost and quantity as integers to be able to calculate the value
            shoe_list.append(shoe) # adds each object to list
    except FileNotFoundError as error: # except for file not found
        print (error)
    except IndexError as error:
        print (error)
    finally:
        if f is not None:
            f.close() # to close the file

def  capture_shoes (): # function to add shoe object with all its variable given as inputs
    try:
        while True: # to make sure an input is given
            country = input ("Please enter country name: ").title() # user input for the country name and first letter capital
            if len (country) -1 > 0 : # to make sure it is not left blank
                break
            else:
                print ("**You have to enter a country name**")
        while True: # to make sure an input is given
            code = input ("Please enter SKU code: ")
            if len (code) -1 > 0 : # to make sure it is not left blank
                break
            else:
                print ("**You have to enter a SKU code**")
        while True: # to make sure an input is given
            product = input ("Please enter product name: ")
            if len (product) -1 > 0: # to make sure it is not left blank
                break
            else:
                print ("**You have to enter the product name**")
        cost = int (input ("Please enter cost: ")) 
        quantity = int (input("Please enter quantity of stock: "))
        shoe = Shoes (country, code, product, cost, quantity)
        shoe_list.append(shoe) # adds the shoe object to list
    except ValueError as error: # value errors for the cost and quantity inputs
        print ("**You have to enter it as numbers**")
        print (error)

def view_all (): # function that display all the stock in a table 
    head = ['Country', 'Code', 'Product','Cost', 'Quantity'] # header of the table
    tabulate_list = [] # list will be used for tabulte
    for shoe in shoe_list:  # for loop that creates a tuple list and adds to tabulate list
        row = shoe.country,shoe.code, shoe.product, shoe.cost, shoe.quantity # creating a tuple for each object in the shoe list 
        tabulate_list.append (row) # add the tuple to the tabulate list
    print (tabulate (tabulate_list, headers = head, tablefmt= 'fancy_grid')) # printing the tabulate list with the header

def re_stock (): # function displaying the lowest stock in tabulate grid and ask if you want to add more stock or not, if yes then it updates the file.
    head = ['Country', 'Code', 'Product','Cost', 'Quantity'] # header of the table
    shoe_min_quaninty = math.inf # shoe minimum variable with postive infinity
    min_shoe = [] # to store the minimum shoe 
    tabulate_list = [] # list will be used for tabulte
    for shoe in shoe_list: # for loop that check shoe quantity agianst postive infity in the first iteration then agianst the other object quantities
        if shoe.get_quantity() < shoe_min_quaninty: # check the object quantity agianst the minimum variable if it is less
            shoe_min_quaninty = shoe.get_quantity() # assigns the shoe quantity to variable
            min_shoe = [shoe] # add only the lowest shoe quantity each iteration
            row = shoe.country,shoe.code, shoe.product, shoe.cost, shoe.quantity # creating a tuple for each object in the shoe list 
    tabulate_list.append (row) # add the tuple to the tabulate list
    print (tabulate (tabulate_list, headers= head, tablefmt= 'fancy_grid')) # printing the tabulate list with the header
    while True: # to make sure to get yes or no input
        re_stock_min = input ("Do you want to add more quantity?(Yes or No): ").lower()
        if re_stock_min == 'yes':
            for shoe in min_shoe: # for loop on the min shoe list that ask for how much quanitny to add then call the class quantity setter
                try:
                    quantity_input = int (input ("Please input new quantity: ")) 
                    shoe.set_quantity (quantity_input)
                    tabulate_list.clear() # clears the tabulte list for so it can be re used
                    row = shoe.country,shoe.code, shoe.product, shoe.cost, shoe.quantity # creating a tuple for each object in the shoe list 
                except ValueError as error:
                    print (error)
                    print ("**You have to enter it as numbers**")
            tabulate_list.append (row)  # add the tuple to the tabulate list
            print (tabulate (tabulate_list, headers= head, tablefmt= 'fancy_grid')) # printing the tabulate list with the header
            update_stock() # calls the function to update the file
            break
        if re_stock_min == 'no': 
            break
        else: # incase an inccoret was given to the yes or no input
            Choice_error = ['Input error, try agian'] 
        print (tabulate([Choice_error],headers =(["Oops!"]), tablefmt = 'fancy_grid'))

def search_shoe (): # function that allows user to search for a shoe by SKU code and then displays it in tabulate grid
    head = ['Country', 'Code', 'Product','Cost', 'Quantity', 'Status']
    tabulate_shoe = []
    while True: # to make sure an input is given
        searched_for_shoe = input ("Please enter shoe code: ").upper()
        if len (searched_for_shoe) -1 > 0: # to make sure it is not left blank
            break
        else: 
            print ("**You have to enter a SKU code**")
        for shoe in shoe_list: # for loop that iterates over the list to find to match the  SKUcode
            if shoe.code == searched_for_shoe: # if code is matched
                row = shoe.country,shoe.code, shoe.product, shoe.cost, shoe.quantity # creating a tuple for the object 
                tabulate_shoe = row # assigning the tabulte to the tuple
                print (tabulate ([tabulate_shoe], headers= head, tablefmt= 'fancy_grid')) # printing the tabulate list with the header
                break
        else: # else for is the code is not in stock and print the message using tabulate
            not_in_stock = ['Shoe code not in stock']
            print (tabulate([not_in_stock],headers =(["Inventory Managment"]), tablefmt = 'fancy_grid'))

def value_per_item():
    head = ['Country', 'Code', 'Product','Cost', 'Quantity', 'Value ']  # header of the table
    shoe_list_value = [] # used to store all object list plus their values in a new coloumn, to tabulate
    for shoe in shoe_list: # for loop for all the obects in the list
        shoe.value = shoe.get_quantity() * shoe.get_cost() # value equation
        row = shoe.country,shoe.code, shoe.product, shoe.cost, shoe.quantity,shoe.value # creating a tuple for the tabulate
        shoe_list_value = shoe_list_value + [row] # adding a new row each iteration
    print (tabulate (shoe_list_value, headers= head, tablefmt= 'fancy_grid')) # printing the tabulate list with the header

def highest_qty ():
    head = ['Country', 'Code', 'Product','Cost', 'Quantity', 'Status'] # header of the table
    shoe_max_quaninty = -math.inf # shoe max with a negative infinity 
    max_shoe = [] # store the shoe with the maxmimum quanitiy
    for shoe in shoe_list: # for loop that check shoe quantity agianst negative infity in the first iteration then agianst the other object quantities
        if shoe.get_quantity() > shoe_max_quaninty: # check the object quantity agianst the maximum variable if it is more
            shoe_max_quaninty = shoe.get_quantity() # add only the highest shoe quantity each iteration
            shoe.status = 'On sale' 
            row = shoe.country,shoe.code, shoe.product, shoe.cost, shoe.quantity, shoe.status # creating a tuple for the tabulate with on sale in a new coloumn
            max_shoe=row # creating a tuple for each object in the shoe list 
    print (tabulate ([max_shoe], headers= head, tablefmt= 'fancy_grid')) # printing the maximum shoe list with the header


# core of the program with a while loop that runs untill the user chooses to quit,  meanu options are displayed in a tabulte grid
while user_choice != 7:
    if file_reader_counter == 0: # as soon the program run it call the read file and creats the object list only once
        read_shoes_data()
        file_reader_counter += 1
    else:
        try:
            print ("") # display
            menu_options = ['Please choose a number:\n 1 - Enter a new shoe\n 2 - View all\n 3 - Restock\n 4 - Search shoe\n 5 - Shoe values\n 6 - Highest shoe quantity\n 7 - Quit\n ']
            print (tabulate([menu_options],headers =(["Shoes Are Us!\nInventory Managment"]), tablefmt = 'fancy_grid'))
            print ("") # display
            user_choice = int (input("Enter number here: "))
            if user_choice == 1:
                print ("") # display
                capture_shoes ()
                print ("") # display
            elif user_choice == 2:
                print ("") # display
                view_all ()
                print ("") # display
            elif user_choice == 3:
                print ("") # display
                re_stock ()
                print ("") # display
            elif user_choice == 4:
                print ("") # display
                search_shoe ()
                print ("") # display
            elif user_choice == 5:
                print ("") # display
                value_per_item()
                print ("") # display
            elif user_choice == 6:
                print ("") # display
                highest_qty ()
                print ("") # display
            elif user_choice == 7:
                print ("") # display
                print("Goodbye")
                print ("") # display
            else: # if a wrong number is entered, displays the error in tabulate grid
                print ("") # display
                Choice_error = ['Input error, try agian']
                print (tabulate([Choice_error],headers =(["Oops!"]), tablefmt = 'fancy_grid'))
                print ("") # display
        except ValueError as error: # for a wrong charachter or left blank, displays the error in tabulate grid
            print ("") # display
            Choice_error = ['You have to input a number from the menu! ']
            print (tabulate([Choice_error],headers =(["Oops!"]), tablefmt = 'fancy_grid'))
            print ("") # display
            print (error)
            print ("") # display