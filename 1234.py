java_dictionary = {
    "Fruit Salad" : 380,
    "Fruit Salad (with yogurt honey and nuts)" : 490,
    "Hot Oatmeal Porridge (with milk or yogurt and choice of honey or strawberries)" : 440,
    "Homemade Granola" : 500,
    "French Toast | Choc Chip, Strawberry Chocolate, Choco Banana" : 550,
    "Brioche French Toast (a single piece of classic french toast)" : 230,
    "Classic" : 550,
    "Single Fluffy Homemade Panckake with Butter and Syrup" : 260,
    "Two Eggs with Toast" : 380,
    "Eggs with Toast and Homefries" : 460,
    "Eggs with Toast and Bacon, ham or Sausage" : 640,
    "Toast with Avocado, Cherry Tomatoes and Balsamic Reduction" :  380,
    "Egg & Cheese" : 460,
    "Egg & Cheese with Bacon, Ham, or Sausage" : 600,
    "Egg & Cheese Sandwich with Bacon, Ham, or Sausage Served with Homefries and Fruit Salad" : 750,
    "Two Eggs with Toast, Homefries, Baked Beans & Your Choice of Bacon, Ham or Sausage" : 740,
    "+ Served with Your Choice of Single House Coffee, Tea or Small Glass of Fresh Juice" : 820,
    "Choc Chip Cookie" : 170,
    "Banana Bread" : 180,
    "Assorted Scones" : 180,
    "Brownie"  : 190,
    "Plain Croissant" : 200,
    "Assorted Muffins" : 210,
    "Cinnamon Roll"  : 220,
    "Chocolate Croissant" : 230,
    "Chicken Pie" : 320,
    "Steak Pie" : 330,
    "Apple Cinnamon Cake" : 190,
    "Black Forest Cake" : 370,
    "Chocolate Fudge Cake" : 370,
    "Carrot Cake" : 370
}

def numbering_function (dictionary):
    finished_dictionary = {}
    count = 1
    for key, value in dictionary.items():
        my_list = [key, value]
        finished_dictionary[str(count) + "."] = my_list
        count += 1
    return finished_dictionary

def java_house_menu_with_user_input(dictionary):
    total = 0
    for key, value in dictionary.items():
        print(key, value[0])
    item_numbers = []
    
    answer = 'n' #Gave answer a default value to simplify code block. Removed the first run of the input code [-2]

    while not (answer == 'y' or answer == 'yes'): #changed the while evaluation to be more robust so as not to end the program prematurely [Modify]
        item = input("Item number? ")
        
        # changed operation order of append and input [Modify]
        item_numbers.append(item) 
        answer = input("Is that all? ") #changed answear variable to answer [Modify]

    print('\n\n') #added a spacing for the final printing of order

    for every_number in item_numbers:
        print(f"That will be a",dictionary[str(every_number) + "."][0])
        total += dictionary[str(every_number) + "."][1]
    print(f"The Total Will Be KES {total}")

java_house_menu_with_user_input(numbering_function(java_dictionary)) 