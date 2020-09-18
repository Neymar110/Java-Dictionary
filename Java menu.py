finished_dictionary = {}
with open("ABC123.txt", "r") as file:
    for line in file:
        key, value = line.split(' : ')
        key = key.strip('"')
        finished_dictionary[key] = int(value[0:3])
    print(finished_dictionary)
def numbering_function (dictionary):
    finished_dictionary1 = {}
    count = 1
    for key, value in dictionary.items():
        my_list = [key, value]
        finished_dictionary1[str(count) + "."] = my_list
        count += 1
    return finished_dictionary1

def java_house_menu_with_user_input(dictionary):
    total = 0
    for key, value in dictionary.items():
        print(key, value[0])
    item_numbers = []
    print("\n")
    answear = "No"
    while answear == "No" or answear == "no" or answear == "n":
        item = input("Item number? ")
        item_numbers.append(item)
        answear = input("Is that all? ")
    print("\n")
    for every_number in item_numbers:
        print(f"That will be a",dictionary[str(every_number) + "."][0])
        total += dictionary[str(every_number) + "."][1]
    print(f"The Total Will Be KES {total}")
java_house_menu_with_user_input(numbering_function(finished_dictionary))

