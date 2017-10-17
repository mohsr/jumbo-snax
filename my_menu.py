"""

my_menu.py
Mohsin Rizvi
Last edited: 10/16/17
Defines the My_Menu class, the Day_Menu class, and the Setting class.

"""
import requests as req
import datetime as time
import sys
import json

class My_Menu:

    def __init__(self):
        # Get the current date and start the repl.
        self.rn = time.datetime.now()
        self.repl()

    def repl(self):
        comms = {"t": "Get today's menus",
                 "w": "Get this week's menus",
                 "f": "Get out your favorite foods",
                 "help": "Get a list of valid commands",
                 "q": "Quit jumbo-snax"}

        print("Welcome to jumbo-snax! Type \"help\" for a list of commands.")
        # The repl below is pretty rough, I should refine it.
        while (True):
            entered = input().strip().lower()
            if entered == "help":
                self.print_dict(comms, "Commands")
            elif entered == "t":
                self.print_day(self.rn)
            elif entered == "w":
                self.print_week(self.rn)
            elif entered == "f":
                self.print_favs()
            elif entered == "q":
                self.quit()
            else:
                print("Invalid command :(")
                continue
            print("What would you like to do now? " +
                  "Type \"help\" for a list of commands.")

    def print_dict(self, comms, dict_name = None):
        if dict_name != None:
            print(("%s: ") % dict_name)
        for i in comms:
            print("  %s\t%s" % (str(i), comms[i]))

    def print_list(self, lst, lst_name = None):
        if lst_name != None:
            print("%s: " % lst_name)
        for i in lst:
            print("    %s" % i)

    def print_day(self, date):
        print("Retrieving data...")
        menu = Day_Menu(date)
        setting = self.get_hall_meal()
        self.print_meal(menu, setting)

    def print_week(self, date):
        pass

    def print_favs(self):
        pass

    def quit(self):
        print("Thanks for using jumbo-snax!")
        sys.exit()

    def get_hall_meal(self):
        halls = ["d", "c", "b"]
        meals = ["b", "l", "d"]
        hall = ""
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
        while meal not in meals:
            print("Which meal time would you like? Type \"b\" for " +
                  "breakfast, \"l\" for lunch, or \"d\" for dinner.")
            meal = input().strip().lower()
            if len(meal) > 0:
                meal = meal[0]
            if meal not in meals:
                print("Invalid command :(")

        return Setting(hall, meal)

    def print_meal(self, menu, setting):
        menus_to_print = []
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

class Day_Menu:

    def __init__(self, date):
        self.dew = req.get("https://tuftsdiningdata.herokuapp.com/menus/" + 
                           "dewick/%d/%d/%d" %
                           (date.day, date.month, date.year)).json()
        self.carm = req.get("https://tuftsdiningdata.herokuapp.com/menus/" + 
                            "carm/%d/%d/%d" %
                            (date.day, date.month, date.year)).json()

    def print_dewick(self):
        pass

    def print_carm(self):
        pass

class Setting:

    def __init__(self, hall, meal):
        self.hall = hall
        self.meal = meal