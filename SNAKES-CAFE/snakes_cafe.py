def snakes_cafe():
    
    print("**************************************")
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**                                  **")
    print("** To quit at any time, type 'quit' **")
    print("**************************************")

    menu={
        "Appetizers":["Wings","Cookies","Spring Rolls"],
        "Entrees":["Salmon","Steak","Meat Tornado Rolls","A Literal Garden"],
        "Desserts":["Ice Cream","Cake","Pie"],
        "Drinks":["Coffee","Tea","Unicorn Tears"]
    }

    for category, items in menu.items():
        print(category)
        print("--------------")
        for item in items:
            print(item)
        print()

    print("***********************************")
    print("** What would you like to order? **")
    print("***********************************")

    order = input("> ")
    ordered={}

    while order != "quit":
        for category, items in menu.items():
            for item in items:
                if order==item:
                    if item in ordered:
                        ordered[item]+=1
                    else:
                        ordered[item]=1

        print("******************************")
        print("** Here is your order:      **")
        for item, count in ordered.items():
            print(f"** {count} order of {item} has been added to your meal **")
        print("******************************")
        order = input("> ")

snakes_cafe()