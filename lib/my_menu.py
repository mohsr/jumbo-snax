"""

my_menu.py
Mohsin Rizvi
Last edited: 10/17/17
Defines the My_Menu class, the Day_Menu class, and the Setting class.

"""
import requests as req
import datetime as time
import sys
import json

# The My_Menu class is used to run the program.
class My_Menu:

    # Purpose:    Create a My_Menu instance to run the program.
    # Parameters: None
    # Return:     Void
    def __init__(self):
        # Get the current date and start the repl.
        self.rn = time.datetime.now()
        self.repl()

    # Purpose:    Runs a REPL for the program.
    # Parameters: None
    # Return:     Void
    def repl(self):
        comms = {"t": "Get today's menus",
                 "w": "Get this week's menus",
                 "f": "Search for your favorite foods",
                 "lf": "Print your favorite foods",
                 "help": "Get a list of valid commands",
                 "q": "Quit jumbo-snax"}

        print("Welcome to jumbo-snax! Type \"help\" for a list of commands.")
        # TODO: The repl below is pretty rough, I should refine it.
        while (True):
            entered = input().strip().lower()
            if entered == "help":
                self.print_dict(comms, "Commands")
            elif entered == "t":
                self.search_day(self.rn)
            elif entered == "w":
                self.search_week(self.rn)
            elif entered == "f":
                self.search_favs()
            elif entered == "lf":
                self.print_favs()
            elif entered == "q":
                self.quit()
            else:
                print("Invalid command :(")
                continue
            print("What would you like to do now? " +
                  "Type \"help\" for a list of commands.")

    # Purpose:    Print a dictionary in an ~elegant~ manner.
    # Parameters: A dictionary to print, and then an optional dictionary
    #             name.
    # Return:     Void
    def print_dict(self, comms, dict_name = None):
        # Print a dictionary name if one is given.
        if dict_name != None:
            print(("%s: ") % dict_name)
        # Print the keys and values.
        for i in comms:
            print("  %s\t%s" % (str(i), comms[i]))

    # Purpose:    Print a list in an ~elegant~ manner.
    # Parameters: A list to print, and then an optional list name.
    # Return:     Void
    def print_list(self, lst, lst_name = None):
        # Print a list name if one is given.
        if lst_name != None:
            print("%s: " % lst_name)
        # Print the elements.
        for i in lst:
            print("    %s" % i)

    # Purpose:    Retrieve and print dining hall data for a certain day.
    # Parameters: A datetime instance to give the day to check for.
    # Return:     Void
    def search_day(self, date):
        print("Retrieving data...")
        # Retrieve the data, get a setting, and print the menu.
        # TODO: This can be improved significantly by retrieving data after
        #       getting the dining halls to search.
        menu = Day_Menu(date)
        setting = self.get_hall_meal()
        self.print_meal(menu, setting)

    # Purpose:    Retrieve and print dining hall data for the next week.
    # Parameters: A datetime type to start printing the week from.
    # Return:     Void
    def search_week(self, date):
        pass

    # Purpose:    Search the next week for your favorite foods, stored in
    #             "favs.json", and print results.
    # Parameters: None
    # Return:     Void
    def search_favs(self):
        pass

    # Purpose:    Print out your favorite foods, stored in "favs.json".
    # Parameters: None
    # Return:     Void
    def print_favs(self):
        pass

    # Purpose:    Quit the program.
    # Parameters: None
    # Return:     Void
    def quit(self):
        print("Thanks for using jumbo-snax!")
        sys.exit()

    # Purpose:    Get a dining hall (or both) and mealtime to search.
    # Parameters: None
    # Return:     A Setting instance with a dining hall code "d", "c", or
    #             "b" for Dewick, Carmichael, and both, as well as a meal
    #             code "b", "l", or "d" for breakfast, lunch, and dinner
    #             respectively.
    def get_hall_meal(self):
        halls = ["d", "c", "b"]
        meals = ["b", "l", "d"]
        hall = ""
        # Retrieve and verify input for dining halls
        while hall not in halls:
            print("Which dining hall would you like to search? " +
                  "Type \"d\" for Dewick, \"c\" for Carmichael, " +
                  "or \"b\" for both.")
            hall = input().strip().lower()
            if len(hall) > 0:
                hall = hall[0]
            if hall not in halls:
                print("Invalid command :(")
        print("Good choice!")
        meal = ""
        # Retrieve and verify input for meal time
        while meal not in meals:
            print("Which meal time would you like? Type \"b\" for " +
                  "breakfast, \"l\" for lunch, or \"d\" for dinner.")
            meal = input().strip().lower()
            if len(meal) > 0:
                meal = meal[0]
            if meal not in meals:
                print("Invalid command :(")

        return Setting(hall, meal)

    # Purpose:    Prints out the menus for a certain dining hall (or both)
    #             for a certain meal time.
    # Parameters: A Day_Menu instance giving menus for Dewick and Carmichael,
    #             and a Setting instance giving the dining hall and meal time
    #             to print for.
    # Return:     Void
    def print_meal(self, menu, setting):
        menus_to_print = []
        # First, decide which dining hall it is and what the meal time is.
        if setting.hall == "c" or setting.hall == "b":
            menus_to_print.append(menu.carm)
        if setting.hall == "d" or setting.hall == "b":
            menus_to_print.append(menu.dew)
        if setting.meal == "b":
            meal_to_print = "Breakfast"
        elif setting.meal == "l":
            meal_to_print = "Lunch"
        elif setting.meal == "d":
            meal_to_print = "Dinner"

        # Print a meal time menu for all selected dining halls.
        for i in menus_to_print:
            if i == menu.carm:
                h_temp = "Carmichael"
            elif i == menu.dew:
                h_temp = "Dewick"

            print("=========================================")
            print("%s %s:" % (h_temp, meal_to_print.lower()))
            print("=========================================")
            # Check for each item type
            for j in i["data"][meal_to_print]:
                # Print the list of items
                self.print_list(i["data"][meal_to_print][j], j)

# The Day_Menu class holds menus for Dewick and Carmichael for a given date.
class Day_Menu:

    # Purpose:    Get menus for Dewick and Carmichael for a given date.
    # Parameters: A datetime instance to give the day to check for.
    # Return:     Void
    def __init__(self, date):
        # TODO: Day_Menu should not initially load both, and should only
        #       load a hall when its data is requested by the user.
        self.dew = req.get("https://tuftsdiningdata.herokuapp.com/menus/" + 
                           "dewick/%d/%d/%d" %
                           (date.day, date.month, date.year)).json()
        self.carm = req.get("https://tuftsdiningdata.herokuapp.com/menus/" + 
                            "carm/%d/%d/%d" %
                            (date.day, date.month, date.year)).json()

# The Setting class holds a dining hall code and a meal time code.
class Setting:

    # Purpose:    Create a Setting instance with a given dining hall code
    #             and meal time code.
    # Parameters: A dining hall code, which is a string that is "d" for
    #             Dewick, "c" for Carmichael, or "b" for both, and a meal
    #             time code, which is either "b" for breakfast, "l" for
    #             lunch, or "d" for dinner.
    def __init__(self, hall, meal):
        self.hall = hall
        self.meal = meal
