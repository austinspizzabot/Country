def displayMenu():
    print("Command Menu: ")
    print("View --> View country name")
    print("Add --> Add a country")
    print("Delete --> Delete a country")
    print("Exit --> Exit program.")
    print()

def display_codes(countries):
    codes = list(countries.keys())
    codes.sort()
    codes_line = "Country codes: "
    for code in codes:
        codes_line += code + " "
    print(codes_line)

def view(countries):
    display_codes(countries)
    code = input("Enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"Country name: {name}. \n")
    else:
        print("There in no country with that code.")
        
def add(countries):
    code = input("Please enter country code: ")
    code = code.upper()
    if code in countries:
        name = countries[code]
        print(f"{name} is already using this code.")
    else:
        name = input("Please enter country name: ")
        name = name.title()
        countries[code] = name
        print(f"{name} was added to the list. \n")
        
def delete(countries):
    code = input("Please enter country code: ")
    code = code.upper()
    if code in countries:
        code = countries.pop(code)
        print(f"Country name entered was deleted.")
    else:
        print("There is no country with that code \n")
        
def main():
    countries = {"AR": "Argentina", "FJ": "Fiji", "IT": "Italy"}
    
    displayMenu()
    while True:
        command = input("Command: ")
        command = command.lower()
        if command == "view":
            view(countries)
        elif command == "add":
            add(countries)
        elif command == "delete":
            delete(countries)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Please enter a valid command from the command list")
 
if __name__ == "__main__":
    main()
            
